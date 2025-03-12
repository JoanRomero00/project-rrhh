import { useNavigate } from "react-router-dom";

export function EmployeeCard( {employee} ) {
  const navigate = useNavigate();
  
  return (
    <div className="p-3 hover:bg-zinc-700 hover:cursor-pointer"
    onClick={() => {
      navigate(`/employees/${employee.id}`);
    }}>
       <div key={employee.id}>
                <h1 className="fond-bold uppercase">{employee.name} {employee.last_name}</h1>
                <p className="text-slade-400">{employee.dni}</p>
                <p>{employee.address}</p>
                <p>{employee.phone}</p>
        </div>
        <hr />
    </div>
  );
}