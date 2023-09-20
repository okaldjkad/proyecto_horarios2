-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 17, 2023 at 10:50 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tec_boletines`
--

-- --------------------------------------------------------

--
-- Table structure for table `alumnos`
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
-- Dumping data for table `alumnos`
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
-- Table structure for table `aulas`
--

CREATE TABLE `aulas` (
  `Tipo_de_aula` varchar(25) NOT NULL,
  `Ubicacion` varchar(25) NOT NULL,
  `Numero` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aulas`
--

INSERT INTO `aulas` (`Tipo_de_aula`, `Ubicacion`, `Numero`) VALUES
('', 'Planta_alta', 0),
('Taller', 'Planta_alta', 3),
('Aula', 'Planta_alta', 2),
('Aula', 'Planta_alta', 3);

-- --------------------------------------------------------

--
-- Table structure for table `boletines__base_de_datos`
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
-- Table structure for table `boletines__dibujo_tecnico`
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
-- Table structure for table `boletines__electronica`
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
-- Table structure for table `boletines__hardware`
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
-- Table structure for table `boletines__historia`
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
-- Dumping data for table `boletines__historia`
--

INSERT INTO `boletines__historia` (`ID`, `CURSO`, `NOTA1`, `NOTA2`, `NOTA3`, `NOTA_DICIE`, `NOTA_FEBRE`, `NOTA_MARZO`, `NOTA_FINAL`) VALUES
(1, '1ro_a', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, '1ro_a', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(3, '1ro_a', NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `boletines__literatura`
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
-- Dumping data for table `boletines__literatura`
--

INSERT INTO `boletines__literatura` (`ID`, `CURSO`, `NOTA1`, `NOTA2`, `NOTA3`, `NOTA_DICIE`, `NOTA_FEBRE`, `NOTA_MARZO`, `NOTA_FINAL`) VALUES
(1, '1ro_a', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, '1ro_a', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(3, '1ro_a', NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `boletines__matematicas`
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
-- Dumping data for table `boletines__matematicas`
--

INSERT INTO `boletines__matematicas` (`ID`, `Alumno`, `CURSO`, `NOTA1`, `NOTA2`, `NOTA3`, `NOTA_DICIE`, `NOTA_FEBRE`, `NOTA_MARZO`, `NOTA_FINAL`) VALUES
(1, '', '1ro_a', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, '', '1ro_a', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(3, '', '1ro_a', NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `boletines__programacion`
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
-- Table structure for table `boletines__sistemas_operativos`
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
-- Table structure for table `boletines__tele_informatica`
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
-- Table structure for table `cursos`
--

CREATE TABLE `cursos` (
  `ID` int(11) NOT NULL,
  `CURSO` varchar(10) NOT NULL,
  `MATERIAS` mediumtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cursos`
--

INSERT INTO `cursos` (`ID`, `CURSO`, `MATERIAS`) VALUES
(1, '1ro_A','matematicasnashe;Literatura;Programacion'),
(2, '1ro_B','matematicas;Literatura;Programacion'),
(3, '1ro_C','matematicas;Literatura;Programacion'),
(4, '1ro_D','matematicas;Literatura;Programacion'),
(5, '1ro_E','matematicas;Literatura;Programacion;ect;ect;ect;ect;ect;ect;ect;ect;ect;ect;ect;ect'),
(6, '2do_A','Historia;Geografia;Ingles'),
(7, '2do_B','Historia;Geografia;Ingles'),
(8, '2do_C','Historia;Geografia;Ingles'),
(9, '2do_D','Historia;Geografia;Ingles'),
(10, '3ro_A','Historia;Literatura;Ciudadania'),
(11, '3ro_B','Historia;Literatura;Ciudadania'),
(12, '3ro_C','Historia;Literatura;Ciudadania'),
(13, '3ro_D','Historia;Literatura;Ciudadania'),
(14, '4to_1ra','Hardware;Salud_y_Adolescencia;Sistemas_Operativos'),
(15, '4to_2da','Hardware;Salud_y_Adolescencia;Sistemas_Operativos'),
(16, '4to_3ra','Hardware;Salud_y_Adolescencia;Sistemas_Operativos'),
(17, '4to_4ta','Hardware;Salud_y_Adolescencia;Sistemas_Operativos'),
(18, '4to_5ta','Hardware;Salud_y_Adolescencia;Sistemas_Operativos'),
(19, '4to_6ta','Hardware;Salud_y_Adolescencia;Sistemas_Operativos'),
(20, '5to_1ra','Hardware;Programacion;TeleInformatica'),
(21, '5to_2da','Hardware;Programacion;TeleInformatica'),
(22, '5to_3ra','Hardware;Programacion;TeleInformatica'),
(23, '5to_4ta','Hardware;Programacion;TeleInformatica'),
(24, '5to_5ta','Hardware;Programacion;TeleInformatica'),
(25, '6to_1ra','Programacion;Analisis_Matematico;Artistica'),
(26, '6to_2da','Programacion;Analisis_Matematico;Artistica'),
(27, '6to_3ra','Programacion;Analisis_Matematico;Artistica'),
(28, '6to_4ta','Programacion;Analisis_Matematico;Artistica'),
(29, '6to_5ta','Programacion;Analisis_Matematico;Artistica'),
(30, '7mo_1ra','Pasantias;Programacion;Hardware'),
(31, '7mo_3ra','Pasantias;Programacion;Hardware'),
(32, '7mo_4ta','Pasantias;Programacion;Hardware');

-- --------------------------------------------------------

--
-- Table structure for table `espacio_curricular`
--

-- --------------------------------------------------------

--
-- Table structure for table `horarios`
--

CREATE TABLE `horarios` (
  `ID_hor` int(11) NOT NULL,
  `Numero_aula` int(4) DEFAULT NULL,
  `Tipo_de_aula` varchar(20) NOT NULL,
  `Horario_e` time NOT NULL,
  `Horario_s` time NOT NULL,
  `Espacio_curricular` varchar(50) NOT NULL,
  `Año` int(11) NOT NULL,
  `Division` varchar(1) NOT NULL,
  `Grupo` varchar(1) NOT NULL,
  `Profesor` varchar(50) NOT NULL,
  `Dia` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `horarios`
--

INSERT INTO `horarios` (`ID_hor`, `Numero_aula`, `Tipo_de_aula`, `Horario_e`, `Horario_s`, `Espacio_curricular`, `Año`, `Division`, `Grupo`, `Profesor`, `Dia`) VALUES
(2, 10, 'Laboratorio', '22:00:00', '23:00:00', 'Programacion', 4, '5', 'A', 'Pasalaqua', 2);

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__1ro_a`
--

CREATE TABLE `inasistencias__1ro_a` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__1ro_b`
--

CREATE TABLE `inasistencias__1ro_b` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__1ro_c`
--

CREATE TABLE `inasistencias__1ro_c` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__1ro_d`
--

CREATE TABLE `inasistencias__1ro_d` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__1ro_e`
--

CREATE TABLE `inasistencias__1ro_e` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__2do_a`
--

CREATE TABLE `inasistencias__2do_a` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__2do_b`
--

CREATE TABLE `inasistencias__2do_b` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__2do_c`
--

CREATE TABLE `inasistencias__2do_c` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__2do_d`
--

CREATE TABLE `inasistencias__2do_d` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__3ro_a`
--

CREATE TABLE `inasistencias__3ro_a` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__3ro_b`
--

CREATE TABLE `inasistencias__3ro_b` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__3ro_c`
--

CREATE TABLE `inasistencias__3ro_c` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__3ro_d`
--

CREATE TABLE `inasistencias__3ro_d` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__4to_1ra`
--

CREATE TABLE `inasistencias__4to_1ra` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__4to_2da`
--

CREATE TABLE `inasistencias__4to_2da` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__4to_3ra`
--

CREATE TABLE `inasistencias__4to_3ra` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__4to_4ta`
--

CREATE TABLE `inasistencias__4to_4ta` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__4to_5ta`
--

CREATE TABLE `inasistencias__4to_5ta` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__4to_6ta`
--

CREATE TABLE `inasistencias__4to_6ta` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__5to_1ra`
--

CREATE TABLE `inasistencias__5to_1ra` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__5to_2da`
--

CREATE TABLE `inasistencias__5to_2da` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__5to_3ra`
--

CREATE TABLE `inasistencias__5to_3ra` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__5to_4ta`
--

CREATE TABLE `inasistencias__5to_4ta` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__5to_5ta`
--

CREATE TABLE `inasistencias__5to_5ta` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__6to_1ra`
--

CREATE TABLE `inasistencias__6to_1ra` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__6to_2da`
--

CREATE TABLE `inasistencias__6to_2da` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__6to_3ra`
--

CREATE TABLE `inasistencias__6to_3ra` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__6to_4ta`
--

CREATE TABLE `inasistencias__6to_4ta` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__6to_5ta`
--

CREATE TABLE `inasistencias__6to_5ta` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__7mo_1ra`
--

CREATE TABLE `inasistencias__7mo_1ra` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__7mo_3ra`
--

CREATE TABLE `inasistencias__7mo_3ra` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inasistencias__7mo_4ta`
--

CREATE TABLE `inasistencias__7mo_4ta` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `APELLIDO` varchar(50) NOT NULL,
  `FECHA` date NOT NULL,
  `TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `materias`
--

CREATE TABLE `materias` (
  `ID` int(11) NOT NULL,
  `MATERIA` varchar(25) DEFAULT NULL,
  `CURSOS` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `materias`
--

INSERT INTO `materias` (`ID`, `MATERIA`, `CURSOS`) VALUES
(121, 'Matematicas', '1ro_a;1ro_b;1ro_c;1ro_d;1ro_e'),
(122, 'Literatura', '1ro_a;1ro_b;1ro_c;1ro_d;1ro_e'),
(123, 'Historia', '1ro_a;1ro_b;1ro_c;1ro_d;1ro_e'),
(124, 'Sistemas Operativos', '5to_1ra;5to_2da;5to_3ra'),
(125, 'Tele Informatica', '5to_1ra;5to_2da;5to_3ra'),
(126, 'Programacion', '5to_2da'),
(127, 'Base de datos', '5to_2da'),
(128, 'Hardware', '5to_1ra;5to_3ra'),
(129, 'Electronica', '5to_1ra;5to_3ra'),
(130, 'Dibujo Tecnico', '5to_4ta;5to_5ta');

-- --------------------------------------------------------

--
-- Table structure for table `profesores`
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
-- Dumping data for table `profesores`
--

INSERT INTO `profesores` (`Id_profesor`, `Nombre`, `Apellido`, `Telefono`, `Tipo_documento`, `Nro_de_documento`, `Correo`, `Direccion`, `Altura`, `Departamento`, `Fecha_nacimiento`) VALUES
(64, 'Sdfds', 'Dsfsfd', '+54 9 2221 23424', 'DU', 322323, 'etwd@.', 'Dfdssd', '24324', 'Piso 7 S', '2005-09-07'),
(68, 'Sdfds', 'Dsfsfd', '+54 9 2221 23424', 'DU', 322323, 'etwd@.', 'Dfdssd', '24324', 'Piso 1 S', '2005-09-07'),
(69, 'Sdfds', 'Dsfsfd', '+54 9 2221 23424', 'DU', 322323, 'etwd@.', 'Dfdssd', '24324', 'Piso 0 S', '2005-09-07');

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `ID` int(11) NOT NULL,
  `Usuario` varchar(20) NOT NULL,
  `Contraseña` varchar(50) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Apellido` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `Cuil` int(11) NOT NULL,
  `tipo` tinyint(1) NOT NULL,
  `materias` mediumtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`ID`, `Usuario`, `Contraseña`, `Nombre`, `Apellido`, `email`, `Cuil`, `tipo`, `materias`) VALUES
(1, 'admin', 'admin', 'tobias', 'bonanno', 'mailprueba@gmail.com', 123456789, 1, NULL),
(2, '1', '1', '1', '1', '1', 0, 1, NULL),
(3, '2', '2', '2', '2', '2', 2, 2, NULL),
(4, '3', '3', '3', '3', '3', 3, 3, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alumnos`
--
ALTER TABLE `alumnos`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CURSO` (`CURSO`);

--
-- Indexes for table `boletines__base_de_datos`
--
ALTER TABLE `boletines__base_de_datos`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CURSO` (`CURSO`);

--
-- Indexes for table `boletines__dibujo_tecnico`
--
ALTER TABLE `boletines__dibujo_tecnico`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CURSO` (`CURSO`);

--
-- Indexes for table `boletines__electronica`
--
ALTER TABLE `boletines__electronica`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CURSO` (`CURSO`);

--
-- Indexes for table `boletines__hardware`
--
ALTER TABLE `boletines__hardware`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CURSO` (`CURSO`);

--
-- Indexes for table `boletines__historia`
--
ALTER TABLE `boletines__historia`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CURSO` (`CURSO`);

--
-- Indexes for table `boletines__literatura`
--
ALTER TABLE `boletines__literatura`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CURSO` (`CURSO`);

--
-- Indexes for table `boletines__matematicas`
--
ALTER TABLE `boletines__matematicas`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CURSO` (`CURSO`);

--
-- Indexes for table `boletines__programacion`
--
ALTER TABLE `boletines__programacion`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CURSO` (`CURSO`);

--
-- Indexes for table `boletines__sistemas_operativos`
--
ALTER TABLE `boletines__sistemas_operativos`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CURSO` (`CURSO`);

--
-- Indexes for table `boletines__tele_informatica`
--
ALTER TABLE `boletines__tele_informatica`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CURSO` (`CURSO`);

--
-- Indexes for table `cursos`
--
ALTER TABLE `cursos`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `CURSO` (`CURSO`);

--
-- Indexes for table `horarios`
--
ALTER TABLE `horarios`
  ADD PRIMARY KEY (`ID_hor`);

--
-- Indexes for table `inasistencias__1ro_a`
--
ALTER TABLE `inasistencias__1ro_a`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__1ro_b`
--
ALTER TABLE `inasistencias__1ro_b`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__1ro_c`
--
ALTER TABLE `inasistencias__1ro_c`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__1ro_d`
--
ALTER TABLE `inasistencias__1ro_d`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__1ro_e`
--
ALTER TABLE `inasistencias__1ro_e`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__2do_a`
--
ALTER TABLE `inasistencias__2do_a`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__2do_b`
--
ALTER TABLE `inasistencias__2do_b`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__2do_c`
--
ALTER TABLE `inasistencias__2do_c`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__2do_d`
--
ALTER TABLE `inasistencias__2do_d`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__3ro_a`
--
ALTER TABLE `inasistencias__3ro_a`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__3ro_b`
--
ALTER TABLE `inasistencias__3ro_b`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__3ro_c`
--
ALTER TABLE `inasistencias__3ro_c`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__3ro_d`
--
ALTER TABLE `inasistencias__3ro_d`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__4to_1ra`
--
ALTER TABLE `inasistencias__4to_1ra`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__4to_2da`
--
ALTER TABLE `inasistencias__4to_2da`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__4to_3ra`
--
ALTER TABLE `inasistencias__4to_3ra`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__4to_4ta`
--
ALTER TABLE `inasistencias__4to_4ta`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__4to_5ta`
--
ALTER TABLE `inasistencias__4to_5ta`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__4to_6ta`
--
ALTER TABLE `inasistencias__4to_6ta`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__5to_1ra`
--
ALTER TABLE `inasistencias__5to_1ra`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__5to_2da`
--
ALTER TABLE `inasistencias__5to_2da`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__5to_3ra`
--
ALTER TABLE `inasistencias__5to_3ra`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__5to_4ta`
--
ALTER TABLE `inasistencias__5to_4ta`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__5to_5ta`
--
ALTER TABLE `inasistencias__5to_5ta`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__6to_1ra`
--
ALTER TABLE `inasistencias__6to_1ra`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__6to_2da`
--
ALTER TABLE `inasistencias__6to_2da`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__6to_3ra`
--
ALTER TABLE `inasistencias__6to_3ra`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__6to_4ta`
--
ALTER TABLE `inasistencias__6to_4ta`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__6to_5ta`
--
ALTER TABLE `inasistencias__6to_5ta`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__7mo_1ra`
--
ALTER TABLE `inasistencias__7mo_1ra`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__7mo_3ra`
--
ALTER TABLE `inasistencias__7mo_3ra`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `inasistencias__7mo_4ta`
--
ALTER TABLE `inasistencias__7mo_4ta`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `materias`
--
ALTER TABLE `materias`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `MATERIA` (`MATERIA`);

--
-- Indexes for table `profesores`
--
ALTER TABLE `profesores`
  ADD PRIMARY KEY (`Id_profesor`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `alumnos`
--
ALTER TABLE `alumnos`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `cursos`
--
ALTER TABLE `cursos`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1249;

--
-- AUTO_INCREMENT for table `horarios`
--
ALTER TABLE `horarios`
  MODIFY `ID_hor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `inasistencias__1ro_a`
--
ALTER TABLE `inasistencias__1ro_a`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__1ro_b`
--
ALTER TABLE `inasistencias__1ro_b`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__1ro_c`
--
ALTER TABLE `inasistencias__1ro_c`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__1ro_d`
--
ALTER TABLE `inasistencias__1ro_d`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__1ro_e`
--
ALTER TABLE `inasistencias__1ro_e`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__2do_a`
--
ALTER TABLE `inasistencias__2do_a`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__2do_b`
--
ALTER TABLE `inasistencias__2do_b`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__2do_c`
--
ALTER TABLE `inasistencias__2do_c`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__2do_d`
--
ALTER TABLE `inasistencias__2do_d`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__3ro_a`
--
ALTER TABLE `inasistencias__3ro_a`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__3ro_b`
--
ALTER TABLE `inasistencias__3ro_b`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__3ro_c`
--
ALTER TABLE `inasistencias__3ro_c`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__3ro_d`
--
ALTER TABLE `inasistencias__3ro_d`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__4to_1ra`
--
ALTER TABLE `inasistencias__4to_1ra`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__4to_2da`
--
ALTER TABLE `inasistencias__4to_2da`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__4to_3ra`
--
ALTER TABLE `inasistencias__4to_3ra`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__4to_4ta`
--
ALTER TABLE `inasistencias__4to_4ta`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__4to_5ta`
--
ALTER TABLE `inasistencias__4to_5ta`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__4to_6ta`
--
ALTER TABLE `inasistencias__4to_6ta`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__5to_1ra`
--
ALTER TABLE `inasistencias__5to_1ra`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__5to_2da`
--
ALTER TABLE `inasistencias__5to_2da`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__5to_3ra`
--
ALTER TABLE `inasistencias__5to_3ra`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__5to_4ta`
--
ALTER TABLE `inasistencias__5to_4ta`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__5to_5ta`
--
ALTER TABLE `inasistencias__5to_5ta`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__6to_1ra`
--
ALTER TABLE `inasistencias__6to_1ra`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__6to_2da`
--
ALTER TABLE `inasistencias__6to_2da`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__6to_3ra`
--
ALTER TABLE `inasistencias__6to_3ra`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__6to_4ta`
--
ALTER TABLE `inasistencias__6to_4ta`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__6to_5ta`
--
ALTER TABLE `inasistencias__6to_5ta`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__7mo_1ra`
--
ALTER TABLE `inasistencias__7mo_1ra`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__7mo_3ra`
--
ALTER TABLE `inasistencias__7mo_3ra`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inasistencias__7mo_4ta`
--
ALTER TABLE `inasistencias__7mo_4ta`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `materias`
--
ALTER TABLE `materias`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=411;

--
-- AUTO_INCREMENT for table `profesores`
--
ALTER TABLE `profesores`
  MODIFY `Id_profesor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=70;

--
-- AUTO_INCREMENT for table `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `alumnos`
--
ALTER TABLE `alumnos`
  ADD CONSTRAINT `alumnos_ibfk_1` FOREIGN KEY (`CURSO`) REFERENCES `cursos` (`CURSO`);

--
-- Constraints for table `boletines__base_de_datos`
--
ALTER TABLE `boletines__base_de_datos`
  ADD CONSTRAINT `boletines__base_de_datos_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `alumnos` (`ID`),
  ADD CONSTRAINT `boletines__base_de_datos_ibfk_2` FOREIGN KEY (`CURSO`) REFERENCES `cursos` (`CURSO`);

--
-- Constraints for table `boletines__dibujo_tecnico`
--
ALTER TABLE `boletines__dibujo_tecnico`
  ADD CONSTRAINT `boletines__dibujo_tecnico_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `alumnos` (`ID`),
  ADD CONSTRAINT `boletines__dibujo_tecnico_ibfk_2` FOREIGN KEY (`CURSO`) REFERENCES `cursos` (`CURSO`);

--
-- Constraints for table `boletines__electronica`
--
ALTER TABLE `boletines__electronica`
  ADD CONSTRAINT `boletines__electronica_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `alumnos` (`ID`),
  ADD CONSTRAINT `boletines__electronica_ibfk_2` FOREIGN KEY (`CURSO`) REFERENCES `cursos` (`CURSO`);

--
-- Constraints for table `boletines__hardware`
--
ALTER TABLE `boletines__hardware`
  ADD CONSTRAINT `boletines__hardware_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `alumnos` (`ID`),
  ADD CONSTRAINT `boletines__hardware_ibfk_2` FOREIGN KEY (`CURSO`) REFERENCES `cursos` (`CURSO`);

--
-- Constraints for table `boletines__historia`
--
ALTER TABLE `boletines__historia`
  ADD CONSTRAINT `boletines__historia_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `alumnos` (`ID`),
  ADD CONSTRAINT `boletines__historia_ibfk_2` FOREIGN KEY (`CURSO`) REFERENCES `cursos` (`CURSO`);

--
-- Constraints for table `boletines__literatura`
--
ALTER TABLE `boletines__literatura`
  ADD CONSTRAINT `boletines__literatura_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `alumnos` (`ID`),
  ADD CONSTRAINT `boletines__literatura_ibfk_2` FOREIGN KEY (`CURSO`) REFERENCES `cursos` (`CURSO`);

--
-- Constraints for table `boletines__matematicas`
--
ALTER TABLE `boletines__matematicas`
  ADD CONSTRAINT `boletines__matematicas_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `alumnos` (`ID`),
  ADD CONSTRAINT `boletines__matematicas_ibfk_2` FOREIGN KEY (`CURSO`) REFERENCES `cursos` (`CURSO`);

--
-- Constraints for table `boletines__programacion`
--
ALTER TABLE `boletines__programacion`
  ADD CONSTRAINT `boletines__programacion_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `alumnos` (`ID`),
  ADD CONSTRAINT `boletines__programacion_ibfk_2` FOREIGN KEY (`CURSO`) REFERENCES `cursos` (`CURSO`);

--
-- Constraints for table `boletines__sistemas_operativos`
--
ALTER TABLE `boletines__sistemas_operativos`
  ADD CONSTRAINT `boletines__sistemas_operativos_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `alumnos` (`ID`),
  ADD CONSTRAINT `boletines__sistemas_operativos_ibfk_2` FOREIGN KEY (`CURSO`) REFERENCES `cursos` (`CURSO`);

--
-- Constraints for table `boletines__tele_informatica`
--
ALTER TABLE `boletines__tele_informatica`
  ADD CONSTRAINT `boletines__tele_informatica_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `alumnos` (`ID`),
  ADD CONSTRAINT `boletines__tele_informatica_ibfk_2` FOREIGN KEY (`CURSO`) REFERENCES `cursos` (`CURSO`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
