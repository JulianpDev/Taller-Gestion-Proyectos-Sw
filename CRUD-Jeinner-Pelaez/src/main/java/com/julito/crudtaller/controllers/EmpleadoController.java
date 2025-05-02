package com.julito.crudtaller.controllers;

import com.julito.crudtaller.models.Empleado;
import com.julito.crudtaller.repositories.EmpleadoRepository;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/empleados")
public class EmpleadoController {
    public final EmpleadoRepository repo;

    public EmpleadoController(EmpleadoRepository repo) {
        this.repo = repo;
    }

    @GetMapping
    public List<Empleado> listar() {
        return repo.findAll();
    }

    @GetMapping("/{id}")
    public Empleado obteernPorId(@PathVariable Long id) {
        return repo.findById(id).orElse(null);
    }

    @PostMapping
    public Empleado crear(@RequestBody Empleado empleado){
        return repo.save(empleado);
    }

    @PutMapping("/{id}")
    public Empleado actualizar(@PathVariable Long id, @RequestBody Empleado empleado){
        Empleado emp = repo.findById(id).orElse(null);
        emp.setNombre(empleado.getNombre());
        return repo.save(emp);
    }

    @DeleteMapping("/{id}")
    public void eliminar(@PathVariable Long id){
        repo.deleteById(id);
    }
}
