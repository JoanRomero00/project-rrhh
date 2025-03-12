import { Link } from "react-router-dom";

export function Navigation() {
  return (
    <div className="bg-rose-200 flex justify-between py-3 items-center">
      <Link to="/employees">
        <h1 className="font-bold text-3xl ms-4">Employees App</h1>
      </Link>
      <button className="bg-rose-500 p-3 rounded-lg me-4">
        <Link to="/employees-create">Create Employe</Link>
      </button>
    </div>
  );
}