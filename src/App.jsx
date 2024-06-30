import { BrowserRouter, Routes, Route } from "react-router-dom";
import { CanchaPage } from "./pages/CanchaPage";
import { LoginPage } from "./pages/LoginPage";
import { RegisterPage } from "./pages/RegisterPage";

function App() {
  return (

    <BrowserRouter>

        <Routes>

          <Route path="/listadoCancha" element={<CanchaPage/>}/>
          <Route path="/login" element={<LoginPage/>}/>
          <Route path="/register" element={<RegisterPage/>}/>
        </Routes>

    </BrowserRouter>

  );
}

export default App;
