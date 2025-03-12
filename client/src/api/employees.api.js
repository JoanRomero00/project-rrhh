import axios from "axios";

const URL =
  process.env.NODE_ENV === "production"
    ? import.meta.env.VITE_BACKEND_URL
    : "http://localhost:8000";

console.log(URL);
const employeesApi = axios.create({
  baseURL: `${URL}/api/employees`,
});

export const getAllEmployees = () => employeesApi.get("/");

export const getEmployee = (id) => employeesApi.get(`/${id}`);

export const createEmployee = (employee) => employeesApi.post("/", employee);

export const updateEmployee = (id, employee) => employeesApi.put(`/${id}/`, employee);

export const deleteEmployee = (id) => employeesApi.delete(`/${id}/`);