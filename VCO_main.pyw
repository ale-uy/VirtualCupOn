from VCO_design import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pymysql


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.inlog = False
        self.inloge = False
        self.Id = ""
        self.Ide = ""
        self.contenedor.setCurrentIndex(1)
        self.sesion.clicked.connect(self.logon)
        self.sesion_2.clicked.connect(self.bussiness_login)
        self.registrarse.clicked.connect(self.register)
        self.inicio.clicked.connect(self.start)
        self.servicios.clicked.connect(self.service)
        self.cupones.clicked.connect(self.cupons)
        self.ayuda.clicked.connect(self.helps)
        self.login.clicked.connect(self.log_in)
        self.eliminar.clicked.connect(self.erase)
        self.empresas.clicked.connect(self.bussiness)
        self.empresa_pagina.clicked.connect(self.bussiness_logon)
        self.empresa_perfil.clicked.connect(self.bussiness_logon)
        self.empresas_2.clicked.connect(self.bussiness_erase)
        self.empresa_registrar.clicked.connect(self.bussiness_register)
        self.eliminar_no.clicked.connect(self.undelete)
        self.eliminar_si.clicked.connect(self.delete)

    def log_in(self):
        self.contenedor.setCurrentIndex(0)
        if self.inloge == False:
            if self.inlog == True:
                self.inlog = False
                self.login.setText("Login")
                self.alerta.setText("Sesión cerrada con éxito")
                self.Id = ""
                self.usuario.setText("")
                self.inicio.setText("Inicio")
                self.servicios.setEnabled(False)
                self.cupones.setEnabled(False)
                self.ayuda.setEnabled(False)
                self.registrarse.setEnabled(True)
                self.sesion.setEnabled(True)
                self.contrasena.setEnabled(True)
                self.mail.setEnabled(True)
                self.empresas.setEnabled(True)
            else:
                self.alerta.setText("Ingrese Usuario y contraseña para iniciar sesión")
        else:
            self.inloge = False
            self.Ide = ""
            self.usuario.setText("")
            self.login.setText("Login")
            self.alerta.setText("Sesión cerrada con éxito")
            self.alerta_2.setText("")
            self.inicio.setText("Inicio")
            self.servicios.setEnabled(False)
            self.cupones.setEnabled(False)
            self.ayuda.setEnabled(False)
            self.registrarse.setEnabled(True)
            self.sesion.setEnabled(True)
            self.empresas_2.setEnabled(False)
            self.mail_2.setEnabled(True)
            self.contrasena_2.setEnabled(True)
            self.registrarse.setEnabled(True)
            self.sesion.setEnabled(True)
            self.empresa_clave.setEnabled(True)
            self.empresa_direccion.setEnabled(True)
            self.empresa_email.setEnabled(True)
            self.empresa_nombre.setEnabled(True)
            self.empresa_postal.setEnabled(True)
            self.empresa_registrar.setEnabled(True)
            self.empresa_rubro.setEnabled(True)
            self.eliminar.setEnabled(True)
            self.sesion_2.setText("Iniciar Sesión")
            self.empresa_pagina.setText("")
        
    def logon(self):
        ema = self.mail.text()
        pas = self.contrasena.text()
        user = (ema.lower(), pas)
        try:
            database = pymysql.connect("remotemysql.com", "2mdSDqeLw5", "2FOXu6dfZd", "2mdSDqeLw5")
            cur = database.cursor()
            cur.execute("SELECT Mail, Pass FROM Usuarios")
            log = dict(cur.fetchall())
            if user[0] in log.keys() and user[1] == log[user[0]]:
                self.alerta.setText("Login realizado con exito")
                self.inlog = True
                self.Id = ema
                self.usuario_mail.setText(ema)
                self.usuario_clave.setText(pas)
                self.servicios.setEnabled(True)
                self.cupones.setEnabled(True)
                self.ayuda.setEnabled(True)
                self.registrarse.setEnabled(False)
                self.sesion.setEnabled(False)
                self.contrasena.setEnabled(False)
                self.mail.setEnabled(False)
                self.empresas.setEnabled(False)
                self.login.setText("Logout")
                self.inicio.setText("Mi Perfil")
                self.usuario.setText("Usuario: "+self.Id)
            elif user[0] in log.keys() and not user[1] == log[user[0]]:
                self.alerta.setText("La contraseña es incorrecta")
            else:
                self.alerta.setText("Usuario incorrecto, por favor registrese haciendo click abajo")
            database.close()
        except Exception as e:
            print(e)
            self.alerta.setText("Se Necesita Conexion a Internet...")

    def register(self):
        ema = self.mail.text()
        pas = self.contrasena.text()
        user = (ema, pas)
        try:
            database = pymysql.connect("remotemysql.com", "2mdSDqeLw5", "2FOXu6dfZd", "2mdSDqeLw5")
            cur = database.cursor()
            cur.execute("SELECT Mail, Pass FROM Usuarios")
            log = dict(cur.fetchall())
            if user[0] in log.keys():
                self.alerta.setText("El usuario ya existe")
            elif user[0] not in log.keys() and "@" not in str(user[0]):
                self.alerta.setText("El mail ingresado no es válido")
            elif user[0] not in log.keys() and "." not in str(user[0]):
                self.alerta.setText("El mail ingresado no es válido")
            elif user[0] not in log.keys() and len(user[0]) < 6:
                self.alerta.setText("El mail ingresado no es válido")
            elif user[0] not in log.keys() and len(user[0]) < 6:
                self.alerta.setText("La contraseña es demasiado corta, 6 caracteres mínimo")
            else:
                cur.execute("INSERT INTO Usuarios VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(ema, pas, "", "", ""))
                database.commit()
                self.alerta.setText("Usuario creado con exito")
            database.close()
        except Exception as e:
            print(e)
            self.alerta.setText("Se Necesita Conexion a Internet...")

    def erase(self):
        self.eliminar_texto.setText("Está a un paso de eliminar su cuenta, está seguro?")
        self.eliminar_si.setEnabled(True)
        self.eliminar_si.setFlat(False)
        self.eliminar_no.setEnabled(True)
        self.eliminar_no.setFlat(False)
    def delete(self):
        Id = self.Id
        try:
            self.contenedor.setCurrentIndex(0)
            database = pymysql.connect("remotemysql.com", "2mdSDqeLw5", "2FOXu6dfZd", "2mdSDqeLw5")
            cur = database.cursor()
            cur.execute("DELETE FROM Usuarios WHERE Mail = '{0}'".format(Id))
            database.commit()
            self.log_in()
            self.alerta.setText("CUENTA ELIMINADA CON EXITO")
            self.undelete()
            database.close()
        except Exception as e:
            print(e)
    def undelete(self):
        self.eliminar_texto.setText("")
        self.eliminar_si.setEnabled(False)
        self.eliminar_no.setEnabled(False)
        self.eliminar_si.setFlat(True)
        self.eliminar_no.setFlat(True)

    def bussiness(self):
        self.page_empresasSign.setEnabled(True)
        self.contenedor.setCurrentIndex(5)
        
    def bussiness_register(self):
        en = self.empresa_nombre.text()
        em = self.empresa_email.text()
        ep = self.empresa_postal.text()
        ed = self.empresa_direccion.text()
        er = self.empresa_rubro.currentText()
        ec = self.empresa_clave.text()
        et = self.empresa_telefono.text()
        ew = self.empresa_web.text()
        try:
            database = pymysql.connect("remotemysql.com", "2mdSDqeLw5", "2FOXu6dfZd", "2mdSDqeLw5")
            cur = database.cursor()
            cur.execute("SELECT Email, Nombre FROM Empresas")
            log = dict(cur.fetchall())
            if em in log.keys():
                self.empresa_pagina.setText("Una empresa ya está registrada con este email")
            elif "@" not in em or "." not in em or len(em) < 6:
                self.empresa_pagina.setText("El email no es válido")
            elif len(ec) < 8:
                self.empresa_pagina.setText("La clave es demasiado corta, minimo 8 caracteres")
            elif len(ep) != 5:
                self.empresa_pagina.setText("El Código Postal no es válido")
            elif len(en) < 1:
                self.empresa_pagina.setText("Debe introducir un nombre para su empresa") 
            else:
                cur.execute("INSERT INTO Empresas VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')".format(en, em, ep, ed, er, ec, et, ew))
                database.commit()
                self.empresa_pagina.setEnabled(True)
                self.empresa_pagina.setText("Registro exitoso! Click aquí para continuar")
            database.close()
        except Exception as e:
            print(e)
            self.empresa_pagina.setText("Se Necesita Conexion a Internet...")

    def bussiness_logon(self):
        self.contenedor.setCurrentIndex(6)
    def bussiness_login(self):
        emae = self.mail_2.text()
        pase = self.contrasena_2.text()
        usere = (emae.lower(), pase)
        if self.inloge == False:
            try:
                database = pymysql.connect("remotemysql.com", "2mdSDqeLw5", "2FOXu6dfZd", "2mdSDqeLw5")
                cur = database.cursor()
                cur.execute("SELECT Email, Password FROM Empresas")
                loge = dict(cur.fetchall())
                if usere[0] in loge.keys() and usere[1] == loge[usere[0]]:
                    self.alerta_2.setText("Login realizado con exito")
                    self.inloge = True
                    self.Ide = emae
                    self.empresa_email_2.setText(emae)
                    self.empresa_clave_2.setText(pase)
                    self.empresas_2.setEnabled(True)
                    self.mail_2.setEnabled(False)
                    self.contrasena_2.setEnabled(False)
                    self.registrarse.setEnabled(False)
                    self.sesion.setEnabled(False)
                    self.empresa_clave.setEnabled(False)
                    self.empresa_direccion.setEnabled(False)
                    self.empresa_email.setEnabled(False)
                    self.empresa_nombre.setEnabled(False)
                    self.empresa_postal.setEnabled(False)
                    self.empresa_registrar.setEnabled(False)
                    self.empresa_rubro.setEnabled(False)
                    self.empresa_pagina.setEnabled(False)
                    self.servicios.setEnabled(True)
                    self.cupones.setEnabled(True)
                    self.ayuda.setEnabled(True)
                    self.registrarse.setEnabled(False)
                    self.sesion.setEnabled(False)
                    self.eliminar.setEnabled(False)
                    self.login.setText("Logout")
                    self.inicio.setText("Mi Perfil")
                    self.sesion_2.setText("Cerrar Sesión")
                    self.usuario.setText("Empresa: " + self.Ide)
                elif usere[0] in loge.keys() and not usere[1] == loge[usere[0]]:
                    self.alerta_2.setText("La contraseña es incorrecta")
                else:
                    self.alerta_2.setText("Debe registrese haciendo click en login y al final de la página")
                database.close()
            except Exception as e:
                print(e)
                self.alerta_2.setText("Se Necesita Conexion a Internet...")
        else:
            self.log_in()
    def bussiness_erase(self):
        Ide = self.Ide
        try:
            database = pymysql.connect("remotemysql.com", "2mdSDqeLw5", "2FOXu6dfZd", "2mdSDqeLw5")
            cur = database.cursor()
            cur.execute("DELETE FROM Empresas WHERE Email = '{0}'".format(Ide))
            database.commit()
            self.log_in()
            self.alerta.setText("LA CUENTA DE SU EMPRESA FUE ELIMINADA CON EXITO")
            database.close()
        except Exception as e:
            print(e)

    def helps(self):
        self.contenedor.setCurrentIndex(4)
       
    #####################################

    def start(self):
        if self.inloge == True:
            self.contenedor.setCurrentIndex(9)
            self.empresa_editar.clicked.connect(self.update_bussine)
        elif self.inlog == True:
            self.contenedor.setCurrentIndex(10)
            self.usuario_editar.clicked.connect(self.update_user)
            #self.cupones_usuarios_actualizar.connect(self.user_cupons_refresh)
            #self.cupones_usuarios_borrar.clicked.connect(self.user_cupons_delete)
        else:
            self.contenedor.setCurrentIndex(1)
    def update_user(self):
        apas = self.usuario_clave.text()
        aced = self.usuario_cedula.text()
        atel = self.usuario_telefono.text()
        apos = self.usuario_postal.text()
        Id = self.Id
        try:
            database = pymysql.connect("remotemysql.com", "2mdSDqeLw5", "2FOXu6dfZd", "2mdSDqeLw5")
            cur = database.cursor()
            if len(apas) < 6:
                self.label_empresa_3.setText("La contraseña es demasiado corta, 6 caracteres mínimo")
            else:
                cur.execute("UPDATE Usuarios SET Pass = '{0}', CI = '{1}', Tel = '{2}', CP = '{3}' WHERE Mail = '{4}'".format(apas, aced, atel, apos, Id))
                database.commit()
                self.label_empresa_3.setText("Aqui puede editar los datos de su Perfil")
                self.contenedor.setCurrentIndex(0)
                self.alerta.setText("Registro actualizado")
            database.close()
        except Exception as e:
            print(e)
    def update_bussine(self):
        aen = self.empresa_nombre_2.text()
        aep = self.empresa_postal_2.text()
        aed = self.empresa_direccion_2.text()
        aer = self.empresa_rubro_2.currentText()
        aec = self.empresa_clave_2.text()
        aet = self.empresa_telefono_2.text()
        aew = self.empresa_web_2.text()
        Ide = self.Ide
        try:
            database = pymysql.connect("remotemysql.com", "2mdSDqeLw5", "2FOXu6dfZd", "2mdSDqeLw5")
            cur = database.cursor()
            if len(aec) < 8:
                self.label_empresa.setText("La clave es demasiado corta, minimo 8 caracteres")
            elif len(aep) != 5:
                self.label_empresa.setText("El Código Postal no es válido")
            elif len(aen) < 1:
                self.label_empresa.setText("Debe introducir un nombre para su empresa") 
            else:
                cur.execute("UPDATE Empresas SET Nombre = '{0}', Postal = '{1}', Direccion = '{2}', Rubro = '{3}', Password = '{4}', Telefono = '{5}', Web = '{6}' WHERE Email = '{7}'".format(aen, aep, aed, aer, aec, aet, aew, Ide))
                database.commit()
                self.label_empresa.setText("Aqui puede editar los datos de su Empresa")
                self.contenedor.setCurrentIndex(0)
                self.alerta.setText("Registro actualizado")
            database.close()
        except Exception as e:
            print(e)
    def user_cupons_delete(self):
        pass
    def user_cupons_refresh(self):
        pass

    def service(self):
        if self.inlog == True:
            self.contenedor.setCurrentIndex(2)
            self.buscar_empresas.clicked.connect(self.service_search)
            self.buscar_empresasViewCup.clicked.connect(self.service_cupons)
        elif self.inloge == True:
            self.contenedor.setCurrentIndex(7)
            #self.cupon_filtrarC.clicked.connect(self.service_filterC)
            #self.cupon_filtrarM.clicked.connect(self.service_filterM)
            #self.cupon_filtrarU.clicked.connect(self.service_filterU)
            #self.cupon_filtrar.clicked.connect(self.service_filter)
            #self.cupon_completado_eliminar.clicked.connect(self.service_deleteC)
            #self.cupon_seleccionado_eliminar.clicked.connect(self.service_deleteS)
    def service_search(self):
        filR = self.buscar_rubro.currentText()
        filP = self.buscar_postal.text()
        try:
            self.buscar_empresasView.clearContents()
            database = pymysql.connect("remotemysql.com", "2mdSDqeLw5", "2FOXu6dfZd", "2mdSDqeLw5")
            cur = database.cursor()
            cur.execute("SELECT Nombre, Postal, Direccion, Telefono, Web FROM Empresas WHERE Rubro = '{0}' AND Postal = '{1}'".format(filR, filP))
            log = cur.fetchall()
            for row_num, row_data in enumerate(log):
                self.buscar_empresasView.insertRow(row_num)
                for col_num, data in enumerate(row_data):
                    self.buscar_empresasView.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(data)))
            database.close()
        except Exception as e:
            print(e)
    def service_cupons(self):
        items = [dato.text() for dato in self.buscar_empresasView.selectedItems()]
        try:
            a = items[0]
            self.cuponesViewU.clearContents()
            database = pymysql.connect("remotemysql.com", "2mdSDqeLw5", "2FOXu6dfZd", "2mdSDqeLw5")
            cur = database.cursor()
            cur.execute("SELECT Email FROM Empresas WHERE Nombre = '{0}'".format(a))
            loge = cur.fetchall()[0][0]
            cur.execute("SELECT Articulo, Descuento, Metodo, Observacion FROM Cupones WHERE Email = '{0}'".format(loge))
            log = cur.fetchall()
            for row_num, row_data in enumerate(log):
                self.cuponesViewU.insertRow(row_num)
                for col_num, data in enumerate(row_data):
                    self.cuponesViewU.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(data)))
            database.close()
            self.contenedor.setCurrentIndex(3)
        except Exception as e:
            print(e)
    def service_filterC(self):
        pass
    def service_filterM(self):
        pass
    def service_filterU(self):
        pass
    def service_filter(self):
        pass
    def service_deleteC(self):
        pass
    def service_deleteS(self):
        pass

    def cupons(self):
        if self.inlog == True:
            self.contenedor.setCurrentIndex(3)
            #self.cupon_buscar.clicked.connect(self.search_cupon)
            #self.cupon_interes_clicked.connect(self.search_addme)
        elif self.inloge == True:
            self.contenedor.setCurrentIndex(8)
            self.cupon_agregar.clicked.connect(self.cupons_add)
            self.cupon_actualizar.clicked.connect(self.cupons_refresh)
            self.cupon_borrar.clicked.connect(self.cupons_delete)
    def cupons_add(self):
        art = self.cupon_articulo.text()
        des = self.cupon_descuento.text()
        met = self.cupon_metodo.currentText()
        obs = self.cupon_observacion.text()
        Ide = self.Ide
        try:
            database = pymysql.connect("remotemysql.com", "2mdSDqeLw5", "2FOXu6dfZd", "2mdSDqeLw5")
            cur = database.cursor()
            cur.execute("INSERT INTO Cupones (Email, Articulo, Descuento, Metodo, Observacion) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(Ide, art, des, met, obs))
            database.commit()
            database.close()
        except Exception as e:
            print(e)
    def cupons_refresh(self):
        Ide = self.Ide
        try:
            self.cuponesViewE.clearContents()
            database = pymysql.connect("remotemysql.com", "2mdSDqeLw5", "2FOXu6dfZd", "2mdSDqeLw5")
            cur = database.cursor()
            cur.execute("SELECT Articulo, Descuento, Metodo, Observacion FROM Cupones WHERE Email = '{0}'".format(Ide))
            log = cur.fetchall()
            for row_num, row_data in enumerate(log):
                self.cuponesViewE.insertRow(row_num)
                for col_num, data in enumerate(row_data):
                    self.cuponesViewE.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(data)))
            database.close()
        except Exception as e:
            print(e)
    def cupons_delete(self):
        Ide = self.Ide
        items = [dato.text() for dato in self.cuponesViewE.selectedItems()]
        a, b, c, d = items[0], items[1], items[2], items[3]
        try:
            database = pymysql.connect("remotemysql.com", "2mdSDqeLw5", "2FOXu6dfZd", "2mdSDqeLw5")
            cur = database.cursor()
            cur.execute("DELETE FROM Cupones WHERE (Email = '{0}' AND Articulo = '{1}' AND Descuento = '{2}' AND Metodo = '{3}' AND Observacion = '{4}')".format(Ide, a, b, c, d))
            database.commit()
            database.close()
        except Exception as e:
            print(e)
    def search_cupon(self):
        pass
    def search_addme(self):
        pass
        
    ####################################



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
