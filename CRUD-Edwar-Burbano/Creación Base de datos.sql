Create DATABASE UsuariosDB;
Go


Use UsuariosDB;
GO

Create TABLE Usuario(
	ID INT IDENTITY(1,1) Primary key,
	Nombre NVARCHAR(100) not null,
	Identificacion NVARCHAR(50) not null UNIQUE
);

GO
