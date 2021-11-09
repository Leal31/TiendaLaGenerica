class productosRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'productos':
            return 'productos'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'productos':
            return 'productos'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'productos':
            return db == 'productos'
        return None
