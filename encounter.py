from fhir.resources.encounter import Encounter
from fhir.resources.reference import Reference
from fhir.resources.period import Period
from fhir.resources.codeableconcept import CodeableConcept

# Crear el recurso FHIR de paciente con parámetros opcionales
def create_encounter_resource(tipo_de_encuentro, name=None, start_time=None, end_time=None, medico=None, motivo_consulta=None, estado=None, diagnosis=None):
    status = estado if estado else "finished"
    class_fhir = {
        "display": tipo_de_encuentro
    }
    encounter = Encounter(status=status, class_fhir=class_fhir)

    if name:
        encounter.subject = Reference.construct(display=name)

    if start_time and end_time:
        encounter.period = Period.construct(start=start_time, end=end_time)

    if medico:
        encounter.participant = [{"individual": Reference.construct(display=medico)}]

    if motivo_consulta:
        encounter.reasonCode = [CodeableConcept.construct(text=motivo_consulta)]

    if diagnosis:
        encounter.diagnosis = [{"condition": {"display": diagnosis}}]

    return encounter