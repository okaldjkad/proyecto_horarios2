-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-09-2023 a las 13:43:04
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Base de datos: `tecnica_2023`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumnos`
--

CREATE TABLE `alumnos` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `CURSO` varchar(10) NOT NULL,
  `GRUPO` varchar(10) NOT NULL,
  `NACIMIENTO` date NOT NULL,
  `TELEFONO` varchar(20) DEFAULT NULL,
  `nro_de_documento` int(10) DEFAULT NULL,
  `Tipo_documento` varchar(25) DEFAULT NULL,
  `calle` varchar(50) DEFAULT NULL,
  `entre_calle1` varchar(50) DEFAULT NULL,
  `entre_calle2` varchar(50) DEFAULT NULL,
  `numeracion` int(8) DEFAULT NULL,
  `departamento` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `alumnos`
--

INSERT INTO `alumnos` (`ID`, `NOMBRE`, `APELLIDO`, `CURSO`, `GRUPO`, `NACIMIENTO`, `TELEFONO`, `nro_de_documento`, `Tipo_documento`, `calle`, `entre_calle1`, `entre_calle2`, `numeracion`, `departamento`) VALUES
(1, 'Alumno', '1', '1ro_A', 'Ninguno', '2000-01-02', '1112345678', 12345678, NULL, NULL, NULL, NULL, NULL, NULL),
(2, 'Alumno', '2', '1ro_A', 'A', '2000-01-02', '1112345678', 12345677, NULL, NULL, NULL, NULL, NULL, NULL),
(3, 'Alumno', '3', '1ro_A', 'B', '2000-01-02', '1112345678', 12345676, NULL, NULL, NULL, NULL, NULL, NULL),
(4, 'Alumno', '4', '1ro_A', 'C', '2000-01-02', '1112345678', 12345675, NULL, NULL, NULL, NULL, NULL, NULL),
(6, 'Alumno', '6', '2do_A', 'A', '2023-09-11', '1123456789', 12345666, NULL, NULL, NULL, NULL, NULL, NULL),
(7, 'Alumno', '5', '1ro_B', 'C', '2023-09-11', '1123456789', 12345667, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `aulas`
--

CREATE TABLE `aulas` (
  `Tipo_de_aula` varchar(25) NOT NULL,
  `Ubicacion` varchar(25) NOT NULL,
  `Numero` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `aulas`
--

INSERT INTO `aulas` (`Tipo_de_aula`, `Ubicacion`, `Numero`) VALUES
('', 'Planta_alta', 0),
('Taller', 'Planta_alta', 3),
('Aula', 'Planta_alta', 2),
('Aula', 'Planta_alta', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `boletines__base_de_datos`
--

CREATE TABLE `boletines__base_de_datos` (
  `ID` int(11) NOT NULL,
  `CURSO` varchar(10) NOT NULL,
  `NOTA1` int(2) DEFAULT NULL,
  `NOTA2` int(2) DEFAULT NULL,
  `NOTA3` int(2) DEFAULT NULL,
  `NOTA_DICIE` int(2) DEFAULT NULL,
  `NOTA_FEBRE` int(2) DEFAULT NULL,
  `NOTA_MARZO` int(2) DEFAULT NULL,
  `NOTA_FINAL` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `boletines__dibujo_tecnico`
--

CREATE TABLE `boletines__dibujo_tecnico` (
  `ID` int(11) NOT NULL,
  `CURSO` varchar(10) NOT NULL,
  `NOTA1` int(2) DEFAULT NULL,
  `NOTA2` int(2) DEFAULT NULL,
  `NOTA3` int(2) DEFAULT NULL,
  `NOTA_DICIE` int(2) DEFAULT NULL,
  `NOTA_FEBRE` int(2) DEFAULT NULL,
  `NOTA_MARZO` int(2) DEFAULT NULL,
  `NOTA_FINAL` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `boletines__electronica`
--

CREATE TABLE `boletines__electronica` (
  `ID` int(11) NOT NULL,
  `CURSO` varchar(10) NOT NULL,
  `NOTA1` int(2) DEFAULT NULL,
  `NOTA2` int(2) DEFAULT NULL,
  `NOTA3` int(2) DEFAULT NULL,
  `NOTA_DICIE` int(2) DEFAULT NULL,
  `NOTA_FEBRE` int(2) DEFAULT NULL,
  `NOTA_MARZO` int(2) DEFAULT NULL,
  `NOTA_FINAL` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `boletines__hardware`
--

CREATE TABLE `boletines__hardware` (
  `ID` int(11) NOT NULL,
  `CURSO` varchar(10) NOT NULL,
  `NOTA1` int(2) DEFAULT NULL,
  `NOTA2` int(2) DEFAULT NULL,
  `NOTA3` int(2) DEFAULT NULL,
  `NOTA_DICIE` int(2) DEFAULT NULL,
  `NOTA_FEBRE` int(2) DEFAULT NULL,
  `NOTA_MARZO` int(2) DEFAULT NULL,
  `NOTA_FINAL` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `boletines__historia`
--

CREATE TABLE `boletines__historia` (
  `ID` int(11) NOT NULL,
  `CURSO` varchar(10) NOT NULL,
  `NOTA1` int(2) DEFAULT NULL,
  `NOTA2` int(2) DEFAULT NULL,
  `NOTA3` int(2) DEFAULT NULL,
  `NOTA_DICIE` int(2) DEFAULT NULL,
  `NOTA_FEBRE` int(2) DEFAULT NULL,
  `NOTA_MARZO` int(2) DEFAULT NULL,
  `NOTA_FINAL` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `boletines__historia`
--

INSERT INTO `boletines__historia` (`ID`, `CURSO`, `NOTA1`, `NOTA2`, `NOTA3`, `NOTA_DICIE`, `NOTA_FEBRE`, `NOTA_MARZO`, `NOTA_FINAL`) VALUES
(1, '1ro_a', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, '1ro_a', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(3, '1ro_a', NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `boletines__literatura`
--

CREATE TABLE `boletines__literatura` (
  `ID` int(11) NOT NULL,
  `CURSO` varchar(10) NOT NULL,
  `NOTA1` int(2) DEFAULT NULL,
  `NOTA2` int(2) DEFAULT NULL,
  `NOTA3` int(2) DEFAULT NULL,
  `NOTA_DICIE` int(2) DEFAULT NULL,
  `NOTA_FEBRE` int(2) DEFAULT NULL,
  `NOTA_MARZO` int(2) DEFAULT NULL,
  `NOTA_FINAL` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `boletines__literatura`
--

INSERT INTO `boletines__literatura` (`ID`, `CURSO`, `NOTA1`, `NOTA2`, `NOTA3`, `NOTA_DICIE`, `NOTA_FEBRE`, `NOTA_MARZO`, `NOTA_FINAL`) VALUES
(1, '1ro_a', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, '1ro_a', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(3, '1ro_a', NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `boletines__matematicas`
--

CREATE TABLE `boletines__matematicas` (
  `ID` int(11) NOT NULL,
  `Alumno` varchar(255) NOT NULL,
  `CURSO` varchar(10) NOT NULL,
  `NOTA1` int(2) DEFAULT NULL,
  `NOTA2` int(2) DEFAULT NULL,
  `NOTA3` int(2) DEFAULT NULL,
  `NOTA_DICIE` int(2) DEFAULT NULL,
  `NOTA_FEBRE` int(2) DEFAULT NULL,
  `NOTA_MARZO` int(2) DEFAULT NULL,
  `NOTA_FINAL` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `boletines__matematicas`
--

INSERT INTO `boletines__matematicas` (`ID`, `Alumno`, `CURSO`, `NOTA1`, `NOTA2`, `NOTA3`, `NOTA_DICIE`, `NOTA_FEBRE`, `NOTA_MARZO`, `NOTA_FINAL`) VALUES
(1, '', '1ro_a', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, '', '1ro_a', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(3, '', '1ro_a', NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `boletines__programacion`
--

CREATE TABLE `boletines__programacion` (
  `ID` int(11) NOT NULL,
  `CURSO` varchar(10) NOT NULL,
  `NOTA1` int(2) DEFAULT NULL,
  `NOTA2` int(2) DEFAULT NULL,
  `NOTA3` int(2) DEFAULT NULL,
  `NOTA_DICIE` int(2) DEFAULT NULL,
  `NOTA_FEBRE` int(2) DEFAULT NULL,
  `NOTA_MARZO` int(2) DEFAULT NULL,
  `NOTA_FINAL` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `boletines__sistemas_operativos`
--

CREATE TABLE `boletines__sistemas_operativos` (
  `ID` int(11) NOT NULL,
  `CURSO` varchar(10) NOT NULL,
  `NOTA1` int(2) DEFAULT NULL,
  `NOTA2` int(2) DEFAULT NULL,
  `NOTA3` int(2) DEFAULT NULL,
  `NOTA_DICIE` int(2) DEFAULT NULL,
  `NOTA_FEBRE` int(2) DEFAULT NULL,
  `NOTA_MARZO` int(2) DEFAULT NULL,
  `NOTA_FINAL` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `boletines__tele_informatica`
--

CREATE TABLE `boletines__tele_informatica` (
  `ID` int(11) NOT NULL,
  `CURSO` varchar(10) NOT NULL,
  `NOTA1` int(2) DEFAULT NULL,
  `NOTA2` int(2) DEFAULT NULL,
  `NOTA3` int(2) DEFAULT NULL,
  `NOTA_DICIE` int(2) DEFAULT NULL,
  `NOTA_FEBRE` int(2) DEFAULT NULL,
  `NOTA_MARZO` int(2) DEFAULT NULL,
  `NOTA_FINAL` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cursos`
--

CREATE TABLE `cursos` (
  `ID` int(11) NOT NULL,
  `CURSO` varchar(10) NOT NULL,
  `MATERIAS` mediumtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cursos`
--

INSERT INTO `cursos` (`ID`, `CURSO`, `MATERIAS`) VALUES
(1, '1ro_A', 'matematicas;Literatura;Programacion'),
(2, '1ro_B', 'matematicas;Literatura;Programacion'),
(3, '1ro_C', 'matematicas;Literatura;Programacion'),
(4, '1ro_D', 'matematicas;Literatura;Programacion'),
(5, '1ro_E', 'matematicas;Literatura;Programacion;ect;ect;ect;ect;ect;ect;ect;ect;ect;ect;ect;ect'),
(6, '2do_A', 'Historia;Geografia;Ingles'),
(7, '2do_B', 'Historia;Geografia;Ingles'),
(8, '2do_C', 'Historia;Geografia;Ingles'),
(9, '2do_D', 'Historia;Geografia;Ingles'),
(10, '3ro_A', 'Historia;Literatura;Ciudadania'),
(11, '3ro_B', 'Historia;Literatura;Ciudadania'),
(12, '3ro_C', 'Historia;Literatura;Ciudadania'),
(13, '3ro_D', 'Historia;Literatura;Ciudadania'),
(14, '4to_1ra', 'Hardware;Salud_y_Adolescencia;Sistemas_Operativos'),
(15, '4to_2da', 'Hardware;Salud_y_Adolescencia;Sistemas_Operativos'),
(16, '4to_3ra', 'Hardware;Salud_y_Adolescencia;Sistemas_Operativos'),
(17, '4to_4ta', 'Hardware;Salud_y_Adolescencia;Sistemas_Operativos'),
(18, '4to_5ta', 'Hardware;Salud_y_Adolescencia;Sistemas_Operativos'),
(19, '4to_6ta', 'Hardware;Salud_y_Adolescencia;Sistemas_Operativos'),
(20, '5to_1ra', 'Hardware;Programacion;TeleInformatica'),
(21, '5to_2da', 'Hardware;Programacion;TeleInformatica'),
(22, '5to_3ra', 'Hardware;Programacion;TeleInformatica'),
(23, '5to_4ta', 'Hardware;Programacion;TeleInformatica'),
(24, '5to_5ta', 'Hardware;Programacion;TeleInformatica'),
(25, '6to_1ra', 'Programacion;Analisis_Matematico;Artistica'),
(26, '6to_2da', 'Programacion;Analisis_Matematico;Artistica'),
(27, '6to_3ra', 'Programacion;Analisis_Matematico;Artistica'),
(28, '6to_4ta', 'Programacion;Analisis_Matematico;Artistica'),
(29, '6to_5ta', 'Programacion;Analisis_Matematico;Artistica'),
(30, '7mo_1ra', 'Pasantias;Programacion;Hardware'),
(31, '7mo_3ra', 'Pasantias;Programacion;Hardware'),
(32, '7mo_4ta', 'Pasantias;Programacion;Hardware');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horarios`
--

CREATE TABLE `horarios` (
  `ID_hor` int(11) NOT NULL,
  `Numero_aula` int(4) DEFAULT NULL,
  `Tipo_de_aula` varchar(20) NOT NULL,
  `Horario_e` time NOT NULL,
  `Horario_s` time NOT NULL,
  `Espacio_curricular` varchar(50) NOT NULL,
  `Año` int(11) DEFAULT NULL,
  `Division` varchar(1) NOT NULL,
  `Grupo` varchar(1) NOT NULL,
  `Profesor` varchar(50) NOT NULL,
  `Dia` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `horarios`
--

INSERT INTO `horarios` (`ID_hor`, `Numero_aula`, `Tipo_de_aula`, `Horario_e`, `Horario_s`, `Espacio_curricular`, `Año`, `Division`, `Grupo`, `Profesor`, `Dia`) VALUES
(2, 10, 'Laboratorio', '22:00:00', '23:00:00', 'Programacion', 4, '5', 'A', 'Pasalaqua', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inasistencias`
--

CREATE TABLE `inasistencias` (
  `ID` int(11) NOT NULL,
  `ID_ALUMNO` int(11) NOT NULL,
  `CURSO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `inasistencias`
--

INSERT INTO `inasistencias` (`ID`, `ID_ALUMNO`, `CURSO`, `FECHA`, `TIPO`) VALUES
(1, 1, '1ro_A', '2023-09-20', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materias`
--

CREATE TABLE `materias` (
  `ID` int(11) NOT NULL,
  `MATERIA` varchar(25) DEFAULT NULL,
  `CURSOS` text DEFAULT NULL,
  `Grupo` varchar(9) NOT NULL,
  `Especialidad` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `materias`
--

INSERT INTO `materias` (`ID`, `MATERIA`, `CURSOS`, `Grupo`, `Especialidad`) VALUES
(121, 'Matematicas', '1ro_a;1ro_b;1ro_c;1ro_d;1ro_e', '', ''),
(122, 'Literatura', '1ro_a;1ro_b;1ro_c;1ro_d;1ro_e', '', ''),
(123, 'Historia', '1ro_a;1ro_b;1ro_c;1ro_d;1ro_e', '', ''),
(124, 'Sistemas Operativos', '5to_1ra;5to_2da;5to_3ra', '', ''),
(125, 'Tele Informatica', '5to_1ra;5to_2da;5to_3ra', '', ''),
(126, 'Programacion', '5to_2da', '', ''),
(127, 'Base de datos', '5to_2da', '', ''),
(128, 'Hardware', '5to_1ra;5to_3ra', '', ''),
(129, 'Electronica', '5to_1ra;5to_3ra', '', ''),
(130, 'Dibujo Tecnico', '5to_4ta;5to_5ta', '', ''),
(441, 'Instalaciones Web', '1ro_a;1ro_b;1ro_c;1ro_d;1ro_e', 'Ambos', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesores`
--

CREATE TABLE `profesores` (
  `Id_profesor` int(11) NOT NULL,
  `Nombre` varchar(255) NOT NULL,
  `Apellido` varchar(255) NOT NULL,
  `Telefono` varchar(50) NOT NULL,
  `Tipo_documento` varchar(255) NOT NULL,
  `Nro_de_documento` int(11) NOT NULL,
  `Correo` varchar(50) NOT NULL,
  `Direccion` varchar(50) NOT NULL,
  `Altura` varchar(255) NOT NULL,
  `Departamento` varchar(10) NOT NULL,
  `Fecha_nacimiento` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `profesores`
--

INSERT INTO `profesores` (`Id_profesor`, `Nombre`, `Apellido`, `Telefono`, `Tipo_documento`, `Nro_de_documento`, `Correo`, `Direccion`, `Altura`, `Departamento`, `Fecha_nacimiento`) VALUES
(64, 'Sdfds', 'Dsfsfd', '+54 9 2221 23424', 'DU', 322323, 'etwd@.', 'Dfdssd', '24324', 'Piso 7 S', '2005-09-07'),
(68, 'Sdfds', 'Dsfsfd', '+54 9 2221 23424', 'DU', 322323, 'etwd@.', 'Dfdssd', '24324', 'Piso 1 S', '2005-09-07'),
(69, 'Sdfds', 'Dsfsfd', '+54 9 2221 23424', 'DU', 322323, 'etwd@.', 'Dfdssd', '24324', 'Piso 0 S', '2005-09-07');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `ID` int(11) NOT NULL,
  `Usuario` varchar(20) NOT NULL,
  `Contraseña` varchar(30) DEFAULT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Apellido` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `Cuil` int(11) NOT NULL,
  `tipo` tinyint(1) NOT NULL,
  `materias` mediumtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`ID`, `Usuario`, `Contraseña`, `Nombre`, `Apellido`, `email`, `Cuil`, `tipo`, `materias`) VALUES
(1, 'admin', 'admin', 'tobias', 'bonanno', 'mailprueba@gmail.com', 123456789, 1, NULL),
(2, '1', '1', '1', '1', '1', 0, 1, NULL),
(3, '2', '2', '2', '2', '2', 2, 2, NULL),
(4, '3', '3', '3', '3', '3', 3, 3, NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CURSO` (`CURSO`);

--
-- Indices de la tabla `boletines__base_de_datos`
--
ALTER TABLE `boletines__base_de_datos`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CURSO` (`CURSO`);

--
-- Indices de la tabla `boletines__dibujo_tecnico`
--
ALTER TABLE `boletines__dibujo_tecnico`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CURSO` (`CURSO`);

--
-- Indices de la tabla `boletines__electronica`
--
ALTER TABLE `boletines__electronica`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CURSO` (`CURSO`);

--
-- Indices de la tabla `boletines__hardware`
--
ALTER TABLE `boletines__hardware`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CURSO` (`CURSO`);

--
-- Indices de la tabla `boletines__historia`
--
ALTER TABLE `boletines__historia`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CURSO` (`CURSO`);

--
-- Indices de la tabla `boletines__literatura`
--
ALTER TABLE `boletines__literatura`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CURSO` (`CURSO`);

--
-- Indices de la tabla `boletines__matematicas`
--
ALTER TABLE `boletines__matematicas`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CURSO` (`CURSO`);

--
-- Indices de la tabla `boletines__programacion`
--
ALTER TABLE `boletines__programacion`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CURSO` (`CURSO`);

--
-- Indices de la tabla `boletines__sistemas_operativos`
--
ALTER TABLE `boletines__sistemas_operativos`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CURSO` (`CURSO`);

--
-- Indices de la tabla `boletines__tele_informatica`
--
ALTER TABLE `boletines__tele_informatica`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CURSO` (`CURSO`);

--
-- Indices de la tabla `cursos`
--
ALTER TABLE `cursos`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `CURSO` (`CURSO`);

--
-- Indices de la tabla `horarios`
--
ALTER TABLE `horarios`
  ADD PRIMARY KEY (`ID_hor`);

--
-- Indices de la tabla `inasistencias`
--
ALTER TABLE `inasistencias`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_ALUMNO` (`ID_ALUMNO`),
  ADD KEY `CURSO` (`CURSO`);

--
-- Indices de la tabla `materias`
--
ALTER TABLE `materias`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `MATERIA` (`MATERIA`);

--
-- Indices de la tabla `profesores`
--
ALTER TABLE `profesores`
  ADD PRIMARY KEY (`Id_profesor`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `cursos`
--
ALTER TABLE `cursos`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1345;

--
-- AUTO_INCREMENT de la tabla `horarios`
--
ALTER TABLE `horarios`
  MODIFY `ID_hor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de la tabla `inasistencias`
--
ALTER TABLE `inasistencias`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `materias`
--
ALTER TABLE `materias`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=442;

--
-- AUTO_INCREMENT de la tabla `profesores`
--
ALTER TABLE `profesores`
  MODIFY `Id_profesor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=70;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `alumnos`
--
ALTER TABLE `alumnos`
  ADD CONSTRAINT `alumnos_ibfk_1` FOREIGN KEY (`CURSO`) REFERENCES `cursos` (`CURSO`);

--
-- Filtros para la tabla `boletines__base_de_datos`
--
ALTER TABLE `boletines__base_de_datos`
  ADD CONSTRAINT `boletines__base_de_datos_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `alumnos` (`ID`),
  ADD CONSTRAINT `boletines__base_de_datos_ibfk_2` FOREIGN KEY (`CURSO`) REFERENCES `cursos` (`CURSO`);

--
-- Filtros para la tabla `boletines__dibujo_tecnico`
--
ALTER TABLE `boletines__dibujo_tecnico`
  ADD CONSTRAINT `boletines__dibujo_tecnico_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `alumnos` (`ID`),
  ADD CONSTRAINT `boletines__dibujo_tecnico_ibfk_2` FOREIGN KEY (`CURSO`) REFERENCES `cursos` (`CURSO`);

--
-- Filtros para la tabla `boletines__electronica`
--
ALTER TABLE `boletines__electronica`
  ADD CONSTRAINT `boletines__electronica_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `alumnos` (`ID`),
  ADD CONSTRAINT `boletines__electronica_ibfk_2` FOREIGN KEY (`CURSO`) REFERENCES `cursos` (`CURSO`);

--
-- Filtros para la tabla `boletines__hardware`
--
ALTER TABLE `boletines__hardware`
  ADD CONSTRAINT `boletines__hardware_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `alumnos` (`ID`),
  ADD CONSTRAINT `boletines__hardware_ibfk_2` FOREIGN KEY (`CURSO`) REFERENCES `cursos` (`CURSO`);

--
-- Filtros para la tabla `boletines__historia`
--
ALTER TABLE `boletines__historia`
  ADD CONSTRAINT `boletines__historia_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `alumnos` (`ID`),
  ADD CONSTRAINT `boletines__historia_ibfk_2` FOREIGN KEY (`CURSO`) REFERENCES `cursos` (`CURSO`);

--
-- Filtros para la tabla `boletines__literatura`
--
ALTER TABLE `boletines__literatura`
  ADD CONSTRAINT `boletines__literatura_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `alumnos` (`ID`),
  ADD CONSTRAINT `boletines__literatura_ibfk_2` FOREIGN KEY (`CURSO`) REFERENCES `cursos` (`CURSO`);

--
-- Filtros para la tabla `boletines__matematicas`
--
ALTER TABLE `boletines__matematicas`
  ADD CONSTRAINT `boletines__matematicas_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `alumnos` (`ID`),
  ADD CONSTRAINT `boletines__matematicas_ibfk_2` FOREIGN KEY (`CURSO`) REFERENCES `cursos` (`CURSO`);

--
-- Filtros para la tabla `boletines__programacion`
--
ALTER TABLE `boletines__programacion`
  ADD CONSTRAINT `boletines__programacion_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `alumnos` (`ID`),
  ADD CONSTRAINT `boletines__programacion_ibfk_2` FOREIGN KEY (`CURSO`) REFERENCES `cursos` (`CURSO`);

--
-- Filtros para la tabla `boletines__sistemas_operativos`
--
ALTER TABLE `boletines__sistemas_operativos`
  ADD CONSTRAINT `boletines__sistemas_operativos_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `alumnos` (`ID`),
  ADD CONSTRAINT `boletines__sistemas_operativos_ibfk_2` FOREIGN KEY (`CURSO`) REFERENCES `cursos` (`CURSO`);

--
-- Filtros para la tabla `boletines__tele_informatica`
--
ALTER TABLE `boletines__tele_informatica`
  ADD CONSTRAINT `boletines__tele_informatica_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `alumnos` (`ID`),
  ADD CONSTRAINT `boletines__tele_informatica_ibfk_2` FOREIGN KEY (`CURSO`) REFERENCES `cursos` (`CURSO`);

--
-- Filtros para la tabla `inasistencias`
--
ALTER TABLE `inasistencias`
  ADD CONSTRAINT `inasistencias_ibfk_1` FOREIGN KEY (`ID_ALUMNO`) REFERENCES `alumnos` (`ID`),
  ADD CONSTRAINT `inasistencias_ibfk_2` FOREIGN KEY (`CURSO`) REFERENCES `cursos` (`CURSO`);
COMMIT;
