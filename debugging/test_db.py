import logging
#logging.getLogger('parso.python.diff').disabled = True
import TCDataCollection.models as TCDC
import TCDataProcessing.models as TCDP
import TCFrontEnd.models       as TCFE
from TCDataCollection.models import Source, Resource
from TCDataProcessing.models import Storm, Mission, Sensor
from TCFrontEnd.models       import Product

from django.db import models

logging.getLogger('parso.python.diff').disabled = True


tc_models = []
for mod in [TCDC, TCDP, TCFE]:
    for imported_name in dir(mod):
        imp = getattr(mod, imported_name)
        #print('Checking {} | imp = {}'.format(imported_name, imp))
        if (isinstance(imp, type) and issubclass(imp, models.Model)):
            tc_models.append(imp)

for model in tc_models:
    print('{}\n{}\n\n{}\n\n\n'.format(80*'#', model, model.objects.all()))

resources = TCDC.Resource.objects.all()
res = resources[0]
storm = TCDP.Storm.objects.all()[0]

#res.collect(storm=storm)

