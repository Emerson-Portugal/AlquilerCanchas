import { BrowserRouter, Routes, Route } from "react-router-dom";
import { CanchaPage } from "./pages/CanchaPage";


function App() {
  return (

    <BrowserRouter>

        <Routes>

          <Route path="/listadoCancha" element={<CanchaPage/>}/>

        </Routes>

    </BrowserRouter>

  );
}

export default App;
