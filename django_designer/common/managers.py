from django.db import models

class AppManager(models.Manager):
    def internal(self):
        return self.filter(is_external=False)
    
    def external(self):
        return self.filter(is_external=True)