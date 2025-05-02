package org.example;
import java.io.*;
import java.util.*;

public class EmpleadoCRUD {
    private static final String ARCHIVO = "empleados.txt";

    public static void agregarEmpleado(Empleado e) throws IOException {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(ARCHIVO, true))) {
            bw.write(e.toString());
            bw.newLine();
        }
    }

    public static List<Empleado> listar() throws IOException {
        List<Empleado> lista = new ArrayList<>();
        File archivo = new File(ARCHIVO);
        if (!archivo.exists()) return lista;

        try (BufferedReader br = new BufferedReader(new FileReader(ARCHIVO))) {
            String linea;
            while ((linea = br.readLine()) != null) {
                lista.add(Empleado.fromString(linea));
            }
        }
        return lista;
    }

    public static void editarNombre(String identificacion, String nuevoNombre) throws IOException {
        List<Empleado> empleados = listar();
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(ARCHIVO))) {
            for (Empleado e : empleados) {
                if (e.getIdentificacion().equals(identificacion)) {
                    e.setNombre(nuevoNombre);
                }
                bw.write(e.toString());
                bw.newLine();
            }
        }
    }

    public static void eliminar(String identificacion) throws IOException {
        List<Empleado> empleados = listar();
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(ARCHIVO))) {
            for (Empleado e : empleados) {
                if (!e.getIdentificacion().equals(identificacion)) {
                    bw.write(e.toString());
                    bw.newLine();
                }
            }
        }
    }
}
