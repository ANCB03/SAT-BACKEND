from flask import Flask, jsonify, request

app = Flask(__name__)

# Respuesta simulada para cada combinación de riesgo y nivel{
#@activity_router.route("/", methods=["POST"])
#def createActivity():
#    return instance.createActivity()
#}
def generate_student_response(risk, riskLevel):
    # Simulación de diferentes respuestas según el nivel de riesgo
    if riskLevel == "sin_riesgo":
        return []
    elif riskLevel == "leve":
        return [{"nombre": "miguel", "correo": "miguelangellv@ufps.edu.co"}]
    elif riskLevel == "moderado":
        return [
            {"nombre": "Estudiante 1", "correo": "est1@example.com"},
            {"nombre": "Estudiante 2", "correo": "est2@example.com"},
        ]
    elif riskLevel == "critico":
        return [
            {"nombre": "Estudiante 1", "correo": "est1@example.com"},
            {"nombre": "Estudiante 2", "correo": "est2@example.com"},
            {"nombre": "Estudiante 3", "correo": "est3@example.com"},
        ]

# Endpoints para diferentes combinaciones de riesgo y nivel de riesgo
@app.route('/global_<riskLevel>', methods=['GET'])
def get_global(riskLevel):
    return jsonify(generate_student_response("global", riskLevel))

@app.route('/academico_<riskLevel>', methods=['GET'])
def get_academico(riskLevel):
    return jsonify(generate_student_response("academico", riskLevel))

@app.route('/individual_<riskLevel>', methods=['GET'])
def get_individual(riskLevel):
    return jsonify(generate_student_response("individual", riskLevel))

@app.route('/institucional_<riskLevel>', methods=['GET'])
def get_institucional(riskLevel):
    return jsonify(generate_student_response("institucional", riskLevel))

@app.route('/economico_<riskLevel>', methods=['GET'])
def get_economico(riskLevel):
    return jsonify(generate_student_response("economico", riskLevel))

#actividadeslist

# Respuesta simulada para los riesgos del estudiante
@app.route('/riesgo_0000000', methods=['GET'])
def get_risk_student():
    # Simulamos una respuesta con riesgos y sus puntajes
    response = {
        "riesgos": [
            {"nombre": "global", "puntaje": 80},
            {"nombre": "academico", "puntaje": 1},
            {"nombre": "individual", "puntaje": 1},
            {"nombre": "institucional", "puntaje": 1},
            {"nombre": "economico", "puntaje": 1}
        ]
    }
    return jsonify(response)

faculties_data = [
    {
        "nombre": "Facultad de Ingeniería",
        "programas": ["Ingeniería de Sistemas", "Ingeniería Electrónica"]
    },
    {
        "nombre": "Facultad de Ciencias",
        "programas": ["Matemáticas", "Física"]
    }
]

@app.route('/facultades', methods=['GET'])
def get_faculties():
    return jsonify(faculties_data)
# Datos de ejemplo
students_data = {
    "sistemas_2021_1": [
        {
            "_id": "123456",
            "codigo": "123456",
            "nombre": "Juan",
            "apellido": "Pérez",
            "sexo": "M",
            "correo": "juan.perez@correo.com",
            "rol": "estudiante",
            "programa": "sistemas",
            "telefono": "3001234567",
            "direccion": "Calle Falsa 123",
            "estado": "activo",
            "fechaingreso": "2021-01-15",
            "creditosaprobados": 30,
            "edad": 21,
            "ac012": True,
            "creditostotales": 50,
            "semestre": 3,
            "promedio": 4.0,
            "promedioponderadoacomulado": 3.8,
            "riesgo": 65
        },
        {
            "_id": "654321",
            "codigo": "654321",
            "nombre": "Ana",
            "apellido": "Gómez",
            "sexo": "F",
            "correo": "ana.gomez@correo.com",
            "rol": "estudiante",
            "programa": "sistemas",
            "telefono": "3007654321",
            "direccion": "Avenida Siempre Viva 456",
            "estado": "activo",
            "fechaingreso": "2021-02-01",
            "creditosaprobados": 40,
            "edad": 22,
            "ac012": False,
            "creditostotales": 60,
            "semestre": 4,
            "promedio": 3.7,
            "promedioponderadoacomulado": 3.6,
            "riesgo": 30
        }
    ]
}


@app.route('/<string:program_year_semester>', methods=['GET'])
def get_students(program_year_semester):
    students = students_data.get(program_year_semester)
    if students is None:
        return jsonify({"message": "No se encontraron estudiantes para el período solicitado"}), 404
    return jsonify(students)


# Datos de ejemplo que podrías modificar según tus necesidades
students_data1 = {
    "0000000": [
        {
    "estado": "En curso",
    "fecha": "2024-1",
    "promedio": 3.8
  },
  {
    "estado": "Terminado",
    "fecha": "2023-2",
    "promedio": 4.2
  },
  {
    "estado": "Cancelado",
    "fecha": "2023-1",
    "promedio": 3.8
  }
    ]
}

@app.route('/semestres_<code>', methods=['GET'])
def get_semesters(code):
    student_data1 = students_data1.get(code)
    if student_data1:
        print(student_data1)
        return jsonify(student_data1)
    else:
        return jsonify({"ok": False, "msg": "Student not found", "data": None}), 404


@app.route('/riesgo_<code>', methods=['GET'])
def get_risk(code):
    # Simulación de la respuesta que se devolvería desde un backend real
    mock_risk_response = {
        "123456": {"riesgoGlobal": 0.75},
        "654321": {"riesgoGlobal": 0.60},
        "riesgos": [
            {
                "nombre": "Riesgo Académico",
                "puntaje": 85,
                "items": [
                    {"nombre": "Bajo rendimiento", "valor": 45},
                    {"nombre": "Asistencia baja", "valor": 40}
                ]
            }
        ],
        "riesgoGlobal": 80
    }

    return jsonify(mock_risk_response)


@app.route('/beneficios_<code>', methods=['GET'])
def get_benefits(code):
    # Respuesta simulada para beneficios usando el código dinámico
    # Nota: Estos nombres deben coincidir con los nombres en la base de datos "profit",
    # Por ejemplo: "Amigos académicos", "Tutores Pares", "Beca comedor", "Beca trabajo".
    benefits_response = [
        {
            "nombre": "Amigos academico",
            "riesgo": "academico",
            "fechaFinal": None
        },
        {
            "nombre": "Tutor academico",
            "riesgo": "academico",
            "fechaFinal": None
        },
        {
            "nombre": "Servicio de almuerzo",
            "riesgo": "socioeconomico",
            "fechaFinal": "2024-12-31" # Ejemplo de beneficio inactivo/con fecha final
        },
        {
            "nombre": "Beca trabajo",
            "riesgo": "socioeconomico",
            "fechaFinal": None
        }
    ]
    return jsonify(benefits_response)



@app.route("/nota_<string:exam>", methods=["GET"])
def get_exam_notes(exam):
     # Datos de ejemplo (puedes obtenerlos de tu base de datos)
    course_data = {
        "grupo": "A1",
        "materia": {
            "codigo": "MAT101",
            "creditos": 3,
            "horario": "Lunes y Miércoles, 9:00 - 11:00",
            "nombre": "Matemáticas Básicas",
            "semestre": 1
        },
        "docente": "Juan Pérez",
        "1p": 80,  # Primer parcial
        "2p": 75,  # Segundo parcial
        "3p": 85,  # Tercer parcial
        "exam": 90,  # Examen final
        "df": 70  # Examen de recuperación
    }

    # Crear un diccionario de respuesta con las notas basadas en el examen solicitado
    exam_note = course_data.get(exam)
    
    if exam_note is None:
        # Si el parámetro exam no es reconocido, devolvemos un error
        return jsonify({"ok": False, "msg": "Examen no encontrado"}), 404

    # Respuesta con la nota solicitada
    response_data = {
        "grupo": course_data["grupo"],
        "materia": course_data["materia"],
        "docente": course_data["docente"],
        "nota": exam_note
    }
    return jsonify(response_data)


# Simulación de datos según el tipo de riesgo
risk_data = {
    "critico": [
        {"student_id": "12345", "name": "Juan Perez", "risk_level": "Crítico"},
        {"student_id": "67890", "name": "Ana Gomez", "risk_level": "Crítico"}
    ],
    "leve": [
        {"student_id": "54321", "name": "Luis Ramirez", "risk_level": "Leve"},
        {"student_id": "09876", "name": "Maria Rodriguez", "risk_level": "Leve"}
    ],
    "moderado": [
        {"student_id": "13579", "name": "Carlos López", "risk_level": "Moderado"},
        {"student_id": "24680", "name": "Sandra Suarez", "risk_level": "Moderado"}
    ],
    "ac012": [
        {"student_id": "11111", "name": "Jorge Castro", "module": "AC 012"},
        {"student_id": "22222", "name": "Lucia Gutierrez", "module": "AC 012"}
    ]
}

# Endpoint general para riesgos
@app.route("/<risk>_<string:endpoint>", methods=["GET"])
def get_risk_data_endpoint(risk, endpoint):
    # Esto también cubre peticiones del tipo:
    # /critico_sistemas
    # /leve_sistemas_2021_1
    # /critico_facultad
    data = risk_data.get(risk, [])
    # Validamos si piden "critico_sistemas" ó "critico_1152121_A" simulando el mismo comportamiento
    if "_" in endpoint and getattr(endpoint, "count", lambda x: 0)("_") == 1 and not is_valid_semester(endpoint):
        code, group = endpoint.split("_")
        response_data = [{"course": code, "group": group, **student} for student in data]
    else:
        response_data = data
        
    return jsonify(response_data), 200

def is_valid_semester(string):
    # Validar que si tiene un guion bajo podría ser el "sistemas_2021_1"
    parts = string.split("_")
    return len(parts) >= 2 and parts[-1].isdigit()

# Endpoint para el módulo AC 012
@app.route("/ac012_<code>_<group>", methods=["GET"])
def get_ac012_data(code, group):
    data = risk_data["ac012"]
    response = {
        "ok": True,
        "msg": "Datos de módulo AC 012 obtenidos correctamente",
        "data": [{"course": code, "group": group, **student} for student in data]
    }
    return jsonify(response), 200



@app.route('/<role>_<code>', methods=['GET'])
def get_role_user(role, code):
    # Endpoint simulado para peticiones como `/estudiante_123456`, `/docente_123456`, o `/vicerrector_123456`
    if role not in ["estudiante", "docente", "vicerrector"]:
        # Si no es un rol de los esperados, pasamos y devolvemos 404 (para que Flask no intercepte `/sistemas_2021_1` con esta ruta)
        from werkzeug.exceptions import NotFound
        raise NotFound()

    user_data = {
        "contrasena": "scrypt:32768:8:1$klyRkXYKxP6q8mEZ$052aa228ebcf1a8a2d1e1f13ce...", # Hash simulado
        "correo": f"{role}.{code}@ufps.edu.co",
        "nombre": "Nombre_" + code,
        "apellido": "Apellido_" + role,
        "programa": "sistemas",
        "codigo": code,
        "rol": role,
        "documento": code # Por si usamos documento como id (caso vicerrector)
    }
    return jsonify({"ok": True, "msg": f"Datos del {role} obtenidos correctamente", "data": user_data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8082)
