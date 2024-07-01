import { BrowserRouter, Routes, Route } from "react-router-dom";
import { CanchaPage } from "./pages/CanchaPage";
import { LoginPage } from "./pages/LoginPage";
import { RegisterPage } from "./pages/RegisterPage";
import { ReservaPage } from "./pages/ReservaPage";

function App() {
  return (

    <BrowserRouter>

        <Routes>

          <Route path="/listadoCancha" element={<CanchaPage/>}/>
          <Route path="/login" element={<LoginPage/>}/>
          <Route path="/register" element={<RegisterPage/>}/>
          <Route path="/reserva" element={<ReservaPage/>}/>
        </Routes>

    </BrowserRouter>

  );
}

export default App;
