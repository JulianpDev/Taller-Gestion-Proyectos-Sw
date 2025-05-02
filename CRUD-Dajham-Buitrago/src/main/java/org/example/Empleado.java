package org.example;

import java.io.Serializable;

public class Empleado implements Serializable {
    private String nombre;
    private String identificacion;

    public Empleado(String nombre, String identificacion) {
        this.nombre = nombre;
        this.identificacion = identificacion;
    }

    public String getNombre() {
        return nombre;
    }

    public String getIdentificacion() {
        return identificacion;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return nombre + ";" + identificacion;
    }

    public static Empleado fromString(String linea) {
        String[] partes = linea.split(";");
        return new Empleado(partes[0], partes[1]);
    }
}
