# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Empresas(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombreusuario = models.CharField(db_column='nombreUsuario', unique=True, max_length=45)  # Field name made lowercase.
    claveusuario = models.CharField(db_column='claveUsuario', max_length=45)  # Field name made lowercase.
    nombrepersona = models.CharField(db_column='nombrePersona', max_length=45)  # Field name made lowercase.
    apellidopersona = models.CharField(db_column='apellidoPersona', max_length=45)  # Field name made lowercase.
    perfilcreado = models.IntegerField(db_column='perfilCreado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresas'


class Evaluacionesempresa(models.Model):
    id_evaluacionesempresa = models.AutoField(db_column='id_evaluacionesEmpresa', primary_key=True)  # Field name made lowercase.
    comentarioevaluador = models.TextField(db_column='comentarioEvaluador', blank=True, null=True)  # Field name made lowercase.
    puntuacionservicio = models.IntegerField(db_column='puntuacionServicio')  # Field name made lowercase.
    puntuacionproducto = models.IntegerField(db_column='puntuacionProducto')  # Field name made lowercase.
    fechaevaluacion = models.DateField(db_column='fechaEvaluacion')  # Field name made lowercase.
    id_perfilempresa = models.ForeignKey('Perfilempresa', models.DO_NOTHING, db_column='id_perfilEmpresa', blank=True, null=True)  # Field name made lowercase.
    id_evaluador = models.ForeignKey('Evaluador', models.DO_NOTHING, db_column='id_evaluador', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluacionesEmpresa'


class Evaluador(models.Model):
    id_evaluador = models.AutoField(primary_key=True)
    nombreusuario = models.CharField(db_column='nombreUsuario', max_length=45)  # Field name made lowercase.
    claveusuario = models.CharField(db_column='claveUsuario', max_length=45)  # Field name made lowercase.
    nombrepersona = models.CharField(db_column='nombrePersona', max_length=45)  # Field name made lowercase.
    apellidopersona = models.CharField(db_column='apellidoPersona', max_length=45)  # Field name made lowercase.
    iconoevaluador = models.CharField(db_column='iconoEvaluador', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'evaluador'


class Fichaestadisticasempresa(models.Model):
    id_fichaestadisticasempresa = models.AutoField(db_column='id_fichaEstadisticasEmpresa', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField()
    visitastotales = models.IntegerField(db_column='visitasTotales', blank=True, null=True)  # Field name made lowercase.
    visitasinvitados = models.IntegerField(db_column='visitasInvitados', blank=True, null=True)  # Field name made lowercase.
    visitasevaluadores = models.IntegerField(db_column='visitasEvaluadores', blank=True, null=True)  # Field name made lowercase.
    cantidadcomentarios = models.IntegerField(db_column='cantidadComentarios', blank=True, null=True)  # Field name made lowercase.
    cantidadevaluaciones = models.IntegerField(db_column='cantidadEvaluaciones', blank=True, null=True)  # Field name made lowercase.
    promediopuntuacionservicio = models.DecimalField(db_column='promedioPuntuacionServicio', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    promediopuntuacionproducto = models.DecimalField(db_column='promedioPuntuacionProducto', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    promediocalificaciongeneral = models.IntegerField(db_column='promedioCalificacionGeneral', blank=True, null=True)  # Field name made lowercase.
    crecimientoevaluaciones = models.IntegerField(db_column='crecimientoEvaluaciones', blank=True, null=True)  # Field name made lowercase.
    id_perfilempresa = models.ForeignKey('Perfilempresa', models.DO_NOTHING, db_column='id_perfilEmpresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fichaEstadisticasEmpresa'


class Galeriaempresa(models.Model):
    id_galeriaempresa = models.AutoField(db_column='id_galeriaEmpresa', primary_key=True)  # Field name made lowercase.
    imagen1 = models.CharField(max_length=255)
    imagen2 = models.CharField(max_length=255)
    imagen3 = models.CharField(max_length=255)
    imagen4 = models.CharField(max_length=255)
    id_perfilempresa = models.ForeignKey('Perfilempresa', models.DO_NOTHING, db_column='id_perfilEmpresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'galeriaEmpresa'


class Horariosempresa(models.Model):
    id_horarioempresa = models.AutoField(db_column='id_horarioEmpresa', primary_key=True)  # Field name made lowercase.
    descripcionhorario = models.CharField(db_column='descripcionHorario', max_length=60)  # Field name made lowercase.
    horarioapertura = models.TimeField(db_column='horarioApertura')  # Field name made lowercase.
    horariocierre = models.TimeField(db_column='horarioCierre')  # Field name made lowercase.
    id_perfilempresa = models.ForeignKey('Perfilempresa', models.DO_NOTHING, db_column='id_perfilEmpresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'horariosEmpresa'


class Perfilempresa(models.Model):
    id_perfilempresa = models.AutoField(db_column='id_perfilEmpresa', primary_key=True)  # Field name made lowercase.
    nombreempresa = models.CharField(db_column='nombreEmpresa', max_length=100)  # Field name made lowercase.
    esloganempresa = models.CharField(db_column='esloganEmpresa', max_length=200, blank=True, null=True)  # Field name made lowercase.
    descripcionempresa = models.TextField(db_column='descripcionEmpresa')  # Field name made lowercase.
    direccionempresa = models.CharField(db_column='direccionEmpresa', max_length=200)  # Field name made lowercase.
    telefonoempresa = models.CharField(db_column='telefonoEmpresa', max_length=20)  # Field name made lowercase.
    logoempresa = models.CharField(db_column='logoEmpresa', max_length=255)  # Field name made lowercase.
    id_empresa = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfilEmpresa'


class Productosempresa(models.Model):
    id_productosempresa = models.AutoField(db_column='id_productosEmpresa', primary_key=True)  # Field name made lowercase.
    productoempresa = models.CharField(db_column='productoEmpresa', max_length=60, blank=True, null=True)  # Field name made lowercase.
    descripcionproducto = models.CharField(db_column='descripcionProducto', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id_perfilempresa = models.ForeignKey(Perfilempresa, models.DO_NOTHING, db_column='id_perfilEmpresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productosEmpresa'


class Redessocialesempresa(models.Model):
    id_redessocialesempresa = models.AutoField(db_column='id_redesSocialesEmpresa', primary_key=True)  # Field name made lowercase.
    correoempresa = models.CharField(db_column='correoEmpresa', max_length=150, blank=True, null=True)  # Field name made lowercase.
    paginawebempresa = models.CharField(db_column='paginaWebEmpresa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    instagramempresa = models.CharField(db_column='instagramEmpresa', max_length=30, blank=True, null=True)  # Field name made lowercase.
    facebookempresa = models.CharField(db_column='facebookEmpresa', max_length=50, blank=True, null=True)  # Field name made lowercase.
    whatsappempresa = models.CharField(db_column='whatsappEmpresa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id_perfilempresa = models.ForeignKey(Perfilempresa, models.DO_NOTHING, db_column='id_perfilEmpresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'redesSocialesEmpresa'


class Serviciosempresa(models.Model):
    id_serviciosempresa = models.AutoField(db_column='id_serviciosEmpresa', primary_key=True)  # Field name made lowercase.
    nombreservicio = models.CharField(db_column='nombreServicio', max_length=100)  # Field name made lowercase.
    id_perfilempresa = models.ForeignKey(Perfilempresa, models.DO_NOTHING, db_column='id_perfilEmpresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'serviciosEmpresa'
