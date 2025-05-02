package com.julito.crudtaller.repositories;

import com.julito.crudtaller.models.Empleado;
import org.springframework.data.jpa.repository.JpaRepository;

public interface EmpleadoRepository extends JpaRepository<Empleado, Long> {
}
