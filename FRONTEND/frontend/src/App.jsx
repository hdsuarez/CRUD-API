import { useEffect, useState } from "react";

function App() {

  // Estado para guardar usuarios
  const [usuarios, setUsuarios] = useState([]);

  // Se ejecuta una vez al cargar la página
  useEffect(() => {

    fetch("http://127.0.0.1:8000/usuarios")
      .then((response) => response.json())
      .then((data) => {

        console.log("Datos recibidos:", data);

        setUsuarios(data);

      });

  }, []);

  return (
    <div style={{ padding: "20px" }}>

      <h1>Usuarios desde FastAPI 🚀</h1>

      {usuarios.map((usuario) => (

        <div
          key={usuario.id}
          style={{
            border: "1px solid gray",
            padding: "10px",
            marginBottom: "10px",
            borderRadius: "5px"
          }}
        >
          <h3>{usuario.nombre}</h3>
          <p>Edad: {usuario.edad}</p>
        </div>

      ))}

    </div>
  );
}

export default App;