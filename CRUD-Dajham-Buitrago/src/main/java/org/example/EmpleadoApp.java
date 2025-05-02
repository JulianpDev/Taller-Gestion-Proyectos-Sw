package org.example;

import javax.swing.*;
import java.awt.*;
import java.io.IOException;
import java.util.List;

public class EmpleadoApp extends JFrame {
    JTextField txtNombre = new JTextField(15);
    JTextField txtID = new JTextField(15);
    JTextArea area = new JTextArea(10, 30);

    public EmpleadoApp() {
        super("Gestión de Empleados");
        setLayout(new BorderLayout());

        JPanel panelFormulario = new JPanel();
        panelFormulario.add(new JLabel("Nombre:"));
        panelFormulario.add(txtNombre);
        panelFormulario.add(new JLabel("ID:"));
        panelFormulario.add(txtID);

        JPanel panelBotones = new JPanel();
        JButton btnAgregar = new JButton("Agregar");
        JButton btnEditar = new JButton("Editar Nombre");
        JButton btnEliminar = new JButton("Eliminar");
        JButton btnListar = new JButton("Listar");

        panelBotones.add(btnAgregar);
        panelBotones.add(btnEditar);
        panelBotones.add(btnEliminar);
        panelBotones.add(btnListar);

        add(panelFormulario, BorderLayout.NORTH);
        add(panelBotones, BorderLayout.CENTER);
        add(new JScrollPane(area), BorderLayout.SOUTH);

        btnAgregar.addActionListener(e -> agregarEmpleado());
        btnEditar.addActionListener(e -> editarEmpleado());
        btnEliminar.addActionListener(e -> eliminarEmpleado());
        btnListar.addActionListener(e -> listarEmpleados());

        setDefaultCloseOperation(EXIT_ON_CLOSE);
        pack();
        setVisible(true);
    }

    private boolean existeEmpleado(String id) throws IOException {
        List<Empleado> empleados = EmpleadoCRUD.listar();
        return empleados.stream().anyMatch(e -> e.getIdentificacion().equals(id));
    }

    private void agregarEmpleado() {
        String nombre = txtNombre.getText().trim();
        String id = txtID.getText().trim();

        if (nombre.isEmpty() || id.isEmpty()) {
            area.setText("Error: Nombre e identificación son obligatorios.\n");
            return;
        }

        try {
            if (existeEmpleado(id)) {
                area.setText("Error: Ya existe un empleado con esa identificación.\n");
                return;
            }

            EmpleadoCRUD.agregarEmpleado(new Empleado(nombre, id));
            area.setText("Empleado agregado exitosamente.\n");
            txtNombre.setText("");
            txtID.setText("");
        } catch (IOException ex) {
            area.setText("Error al guardar el empleado.\n");
        }
    }

    private void editarEmpleado() {
        String nombre = txtNombre.getText().trim();
        String id = txtID.getText().trim();

        if (nombre.isEmpty() || id.isEmpty()) {
            area.setText("Error: Debe ingresar el nuevo nombre y la identificación.\n");
            return;
        }

        try {
            if (!existeEmpleado(id)) {
                area.setText("Error: No existe ningún empleado con esa identificación.\n");
                return;
            }

            EmpleadoCRUD.editarNombre(id, nombre);
            area.setText("Nombre actualizado correctamente.\n");
            txtNombre.setText("");
            txtID.setText("");
        } catch (IOException ex) {
            area.setText("Error al editar el empleado.\n");
        }
    }

    private void eliminarEmpleado() {
        String id = txtID.getText().trim();

        if (id.isEmpty()) {
            area.setText("Error: Debe ingresar la identificación del empleado a eliminar.\n");
            return;
        }

        try {
            if (!existeEmpleado(id)) {
                area.setText("Error: No existe ningún empleado con esa identificación.\n");
                return;
            }

            EmpleadoCRUD.eliminar(id);
            area.setText("Empleado eliminado correctamente.\n");
            txtNombre.setText("");
            txtID.setText("");
        } catch (IOException ex) {
            area.setText("Error al eliminar el empleado.\n");
        }
    }

    private void listarEmpleados() {
        try {
            List<Empleado> empleados = EmpleadoCRUD.listar();
            if (empleados.isEmpty()) {
                area.setText("No hay empleados registrados.\n");
                return;
            }

            StringBuilder sb = new StringBuilder("Listado de Empleados:\n");
            for (Empleado e : empleados) {
                sb.append("Nombre: ").append(e.getNombre())
                        .append(", ID: ").append(e.getIdentificacion()).append("\n");
            }
            area.setText(sb.toString());
        } catch (IOException ex) {
            area.setText("Error al listar empleados.\n");
        }
    }

    public static void main(String[] args) {
        new EmpleadoApp();
    }
}
