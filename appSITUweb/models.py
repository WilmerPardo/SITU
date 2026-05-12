from django.db import models

class Pasajero(models.Model):
	cedula = models.CharField(max_length=10, blank=False)
	nombre = models.CharField(max_length=10, blank=False)
	imagen = models.ImageField(upload_to='img/%Y/%m/%d/')
	apellido = models.CharField(max_length=30)
	email = models.EmailField()
	def __str__(self):
		return self.cedula

class Tarjeta(models.Model):
	codigo = models.CharField(max_length=6, blank=False)
	monto = models.CharField(max_length=3, blank=False)
	idPasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)
	def __str__(self):
		return f'Tarjeta: {self.codigo} | Pasajero: {str(self.idPasajero)} | Monto Tarjeta: {str(self.monto)}'
                                                                
class Bus(models.Model):
	placa = models.CharField(max_length=7, blank=False)
	cooperativa = models.CharField(max_length=10, blank=False)
	numero = models.DecimalField(max_digits=3, decimal_places=0)
	idTarjeta = models.ManyToManyField(Pasajero, through='Viaje')	
	def __str__(self):
		return self.placa

class Viaje(models.Model):
	pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)
	bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
	costo = models.DecimalField(max_digits=4, decimal_places=2)
	cantidad = models.IntegerField()
	fecha_viaje = models.DateTimeField(auto_now_add=True)
	efectivo = models.BooleanField(default=True)	
	confortViaje = (
		('comodo', 'Comodo'),
		('incomodo', 'Incomodo'),
	)
	tipo = models.CharField(max_length=20, choices=confortViaje, default="")
	def __str__(self):
		return f'Pasajero: {self.pasajero.cedula} | Pasj.Nombre: {self.pasajero.nombre} | Precio: {str(self.costo)} | BusPlaca: {str(self.bus.placa)} | No.Bus: {str(self.bus.numero)}'

class SimularAccesoPago(models.Model):
	numero = models.CharField(max_length=7, blank=False)
	fecha_viaje = models.DateTimeField(auto_now_add=True)
	viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)
	tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
	def __str__(self):
	  return f'Pasajero: {self.viaje.pasajero.nombre}'
