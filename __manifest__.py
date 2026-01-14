{
 'name': 'Gestión de vehículos',
 'version': '1.0',
 'summary': 'Gestión de vehículos de la empresa',
 'description': 'Este módulo gestiona los vehículos disponibles en la empresa.',
 'author': 'Paco Navas',
 'category': 'Tools',
 'depends': ['base'],
 'data': [
    'security/ir.model.access.csv', # Control de acceso
    'views/vehiculo_views.xml', # Vista del módulo
 ],
 'installable': True,
 'application': True,
}