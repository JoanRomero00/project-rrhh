import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { Navigation } from "./components/Navigation";
import { EmployeeFormPage } from "./pages/EmployeFormPage";
import { EmployeesPage } from "./pages/EmployeesPage";
import { Toaster } from "react-hot-toast";

function App() {
  return (
    <BrowserRouter>
      <div className="container-fluid mx-auto">
        <Navigation />
        <Routes>
          {/* redirect to Employees */}
          <Route path="/" element={<Navigate to="/employees" />} />
          <Route path="/employees" element={<EmployeesPage />} />
          <Route path="/employees/:id" element={<EmployeeFormPage />} />
          <Route path="/employees-create" element={<EmployeeFormPage />} />
        </Routes>
        <Toaster />
      </div>
    </BrowserRouter>
  );
}

export default App;
