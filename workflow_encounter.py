from encounter import create_encounter_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir, get_patient_with_identifier

if __name__ == "__main__":
    # Parámetros del paciente (se puede dejar algunos vacíos)
    name="Josefina Perez", 
    start_time = "2023-10-01T10:00:00Z",
    end_time = "2023-10-01T11:00:00Z"
    medico="Carlos Gomez", 
    motivo_consulta="Dolor de panza", 
    tipo_de_encuentro = "Espontanea"
    diagnosis = "Intoxicacion alimentaria"

    # Crear y enviar el recurso de paciente
    encounter = create_encounter_resource(
        tipo_de_encuentro, 
        name = name, 
        start_time = start_time,
        end_time = end_time, 
        medico = medico, 
        motivo_consulta = motivo_consulta,
        diagnosis = diagnosis
    )
    encounter_id = send_resource_to_hapi_fhir(encounter, 'Encounter')
    print(f"Encounter ID: {encounter_id}")

    # Ver el recurso de paciente creado
    if encounter_id:
        get_resource_from_hapi_fhir(encounter_id,'Encounter')