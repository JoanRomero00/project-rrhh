import { useEffect, useState } from "react";
import { getAllEmployees } from "../api/employees.api";
import { EmployeeCard } from "./EmployeeCard";

export function EmployeesList() {

    const [employees, setEmployees] = useState([]);

    useEffect(() => {
        async function loadEmployees() {
            const res = await getAllEmployees();
            setEmployees(res.data);
        }
        loadEmployees();
    }, []);

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {employees.map((employee) => (

            <EmployeeCard key={employee.id} employee={employee} />

        ))}
    </div>
  );
}