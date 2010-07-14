import logging
import os
import shutil

logger = logging.getLogger('BuildLogger')

class LocalFS(object):
    def __init__(self, path):
        self.base_path = path
        if os.path.exists(path):
            raise Exception('"%s" alredy exist' % path)
        os.makedirs(path)
        logger.info('%s created' % path)
    
    def write_file(self, filename, content, options='w'):
        file_path = os.path.join(self.base_path, filename)
        if os.path.exists(file_path):
            raise Exception('"%s" alredy exist' % file_path)
        f = open(file_path, options)
        f.write(content)
        f.close()
        logger.info('%s created' % file_path)
    
    def copy(self, source, local):
        shutil.copy(source, os.path.join(self.base_path, local))
        logger.info('%s copied' % local)


class Package(LocalFS):
    def __init__(self, path):
        super(Package, self).__init__(path)
        self.write_file('__init__.py', '')
    
    def write_module(self, name, content, options='w'):
        self.write_file(name+'.py', content, options)
    
    def child_package(self, name):
        return Package(os.path.join(self.base_path, name))


def append_spaces(block, spaces='    '):
    return [spaces+l for l in block]


class CodeBlock(list):
    def child_block(self):
        block = CodeBlock()
        self.append(block) 
        return block
    
    def function(self, name, args_str):
        self.append('def %s(%s):' % (name, args_str))
        return self.child_block()
    
    def class_(self, name, bases=[]):
        bases_s = ', '.join(bases)
        if len(bases_s) > 0:
            bases_s = '(%s)' % bases_s
        self.append('class %s%s:' % (name, bases_s))
        return self.child_block()
    
    def lines(self, indent=0, indent_str="    "): #4 spaces
        for line in self:
            if isinstance(line, (str, unicode)):
                yield (indent_str*indent) + line
            elif isinstance(line, CodeBlock):
                for l in line.lines(indent+1, indent_str):
                    yield l
            else:
                raise Exception('Unsupported item %s' % line)
