-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 15-08-2023 a las 21:59:45
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `spvrb`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `registrar_detallesventa` ()  DETERMINISTIC UPDATE detallesventa SET idventa=last_id() where idVenta IS NULL$$

--
-- Funciones
--
CREATE DEFINER=`root`@`localhost` FUNCTION `last_id` () RETURNS INT(11) DETERMINISTIC NO SQL BEGIN
DECLARE MAXID int;
SELECT MAX(id) INTO MAXID FROM venta;
RETURN MAXID;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `articulo`
--

CREATE TABLE `articulo` (
  `id` int(11) NOT NULL,
  `cb` varchar(15) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `precio` double NOT NULL,
  `marca` varchar(25) NOT NULL,
  `categoria` int(11) NOT NULL,
  `existencias` int(11) NOT NULL,
  `image` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `articulo`
--

INSERT INTO `articulo` (`id`, `cb`, `nombre`, `precio`, `marca`, `categoria`, `existencias`, `image`) VALUES
(1, 'F14401014710141', 'Camara 300-18', 70, 'Ghira', 7, 15, 'CamaraGira_300-18.jpg'),
(2, 'CAD179179089965', 'Cadena', 150, 'Dazon', 7, 3, 'Cadena_Dazo.jpg'),
(3, '275818IL80SD234', 'Sprock trasero', 130, 'Roda', 7, 2, 'Sprock_Trasero_RODA.jpg'),
(4, 'F0106KR08P988H2', 'Reten de barra de suspención ', 60, 'Italika', 6, 5, 'RetenDeBarraSuspencion.jpg'),
(5, 'F203015578K96T4', 'Guarda Cadena ', 160, 'Italika', 6, 4, 'GuardaCadenaItalika_.jpg'),
(6, 'AM0008TI23TR12R', 'Amortiguador trasero', 350, 'Alessia', 6, 4, 'AmortiguadorTraseroAlessia.jpg'),
(7, '245527ES74A704G', 'Estator ', 310, 'Roda', 5, 10, 'EstatorRoda.jpg'),
(8, 'SWI313ST4678CH7', 'Switch', 70, 'China', 5, 8, 'SwitchChina.jpg'),
(9, 'MAD095ND78ZQ957', 'Mando IZQ derecho', 260, 'Dazon', 5, 3, 'MandoIZQDerechoDazon.jpg'),
(10, '232049RE5037E6N', 'Resorte de peda de freno', 15, 'Roda', 4, 15, 'ResorteDePedaDeFreno.jpg'),
(11, '255212CH1C073F3', 'Chicote freno trasero', 60, 'Roda', 4, 4, 'ChicoteFrenoTrasero.jpg'),
(12, 'F15020072BA127A', 'Balata freno trasero', 90, 'Italika', 4, 6, 'BalataFrenoTrasero.jpg'),
(13, 'E0405KV02L990E3', 'Valvulas', 110, 'Italika', 3, 44, 'Valvulas.jpg'),
(14, '215101BA09C1N90', 'Balacin de levas con soporte', 200, 'Roda', 3, 1, 'BalacinDeLevasConSoporte.jpg'),
(15, '535053CA94V3L05', 'Caja de velocidades', 500, 'Roda', 3, 2, 'CajaDeVelocidades.jpg'),
(16, 'F08010043F1L7R0', 'Filtro de aire', 65, 'Italika', 2, 3, 'FiltroDeAire.jpg'),
(17, 'FIL266G4S0L1N48', 'Filtro de gasolina', 15, 'China', 2, 20, 'FiltroDeGasolina.jpg'),
(18, 'SWI312K17C344AD', 'Kit de cerraduras', 180, 'China', 2, 2, 'KitDeCerraduras.jpg'),
(19, '105002MA78BR10L', 'Manubrio', 250, 'Roda', 1, 3, 'MnubrioRoda.jpg'),
(20, 'MAN104P4RM4N194', 'Par manijas ', 200, 'Dazon', 1, 5, 'ParManijas_.jpg'),
(21, '22081044P3D4L4R', 'Pedal de arranque', 140, 'Dazon', 1, 3, 'PedalDeArranque.jpg'),
(22, 'F01010003AC3173', 'Aceite 4T mineral', 110, 'Italika', 8, 50, 'Aceite_4T_mineral.jpg'),
(23, '71800AC3173M189', 'Aceite 4T mineral multigrado', 80, 'Gira', 8, 15, 'Aceite4TMineralMultigrado.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `id` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`id`, `nombre`) VALUES
(1, 'Cuadro'),
(2, 'Misceláneo'),
(3, 'Motor'),
(4, 'Freno'),
(5, 'Eléctrico'),
(6, 'Suspensión'),
(7, 'Tracción'),
(8, 'Aceites');

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `crear_venta`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `crear_venta` (
`idventa` int(11)
,`nombre` varchar(50)
,`cantidad` int(11)
,`subtotal` double
);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detallesventa`
--

CREATE TABLE `detallesventa` (
  `idVenta` int(11) DEFAULT NULL,
  `idArticulo` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Disparadores `detallesventa`
--
DELIMITER $$
CREATE TRIGGER `detallesventa_after_update` AFTER UPDATE ON `detallesventa` FOR EACH ROW UPDATE articulo SET existencias=existencias-NEW.cantidad WHERE NEW.idventa IS NOT NULL AND id=NEW.idarticulo
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedor`
--

CREATE TABLE `proveedor` (
  `id` int(11) NOT NULL,
  `nombre` varchar(25) NOT NULL,
  `apellido` varchar(25) NOT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `direccion` varchar(40) DEFAULT NULL,
  `numdireccion` varchar(3) DEFAULT NULL,
  `colonia` varchar(40) DEFAULT NULL,
  `municipio` varchar(40) DEFAULT NULL,
  `estado` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proveedor`
--

INSERT INTO `proveedor` (`id`, `nombre`, `apellido`, `telefono`, `direccion`, `numdireccion`, `colonia`, `municipio`, `estado`) VALUES
(1, 'Oscar ', 'Pancardo', '2471467890', 'Bulevar Manuel Rincon', '22', 'El alto', 'Santa Ana', 'Tlaxcala'),
(2, 'Luis', 'Molina', '2471347896', 'calle 6 de Septiembre', '22', 'la Joya', 'Tlaxcala', 'Tlaxcala'),
(3, 'Luki', 'Garcia', '2478998790', 'calle 2 de Julio', '333', 'Las rocas', 'San Miguel Contla', 'Tlaxcala');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `idusuario` int(11) NOT NULL,
  `nombreusuario` varchar(45) NOT NULL,
  `contrasena` varchar(160) NOT NULL,
  `is_admin` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`idusuario`, `nombreusuario`, `contrasena`, `is_admin`) VALUES
(1, 'spvrbadmin', 'pbkdf2:sha256:600000$4l1ApYIEzxJzQSrw$9ff988ea4dae685aebc0aa52ced5df34bbcd2005364444a21c186fccf074da14', 1),
(2, 'spvrbcajero', 'pbkdf2:sha256:600000$uFzQ7ZryVwZ9RayD$e59522a069fac49285e37d5087ba1035d16f269e9017a273a71357052ac03a03', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `venta`
--

CREATE TABLE `venta` (
  `id` int(11) NOT NULL,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Disparadores `venta`
--
DELIMITER $$
CREATE TRIGGER `venta_after_insert` AFTER INSERT ON `venta` FOR EACH ROW CALL registrar_detallesventa()
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura para la vista `crear_venta`
--
DROP TABLE IF EXISTS `crear_venta`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `crear_venta`  AS   (select `detallesventa`.`idVenta` AS `idventa`,`articulo`.`nombre` AS `nombre`,`detallesventa`.`cantidad` AS `cantidad`,`detallesventa`.`cantidad` * `articulo`.`precio` AS `subtotal` from (`detallesventa` join `articulo` on(`articulo`.`id` = `detallesventa`.`idArticulo`)) where `detallesventa`.`idVenta` is null)  ;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `articulo`
--
ALTER TABLE `articulo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `cb` (`cb`),
  ADD KEY `fk_cat_id` (`categoria`);

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `detallesventa`
--
ALTER TABLE `detallesventa`
  ADD KEY `idVenta` (`idVenta`),
  ADD KEY `idArticulo` (`idArticulo`);

--
-- Indices de la tabla `proveedor`
--
ALTER TABLE `proveedor`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`idusuario`),
  ADD UNIQUE KEY `idusuario` (`idusuario`),
  ADD UNIQUE KEY `nombreusuario` (`nombreusuario`);

--
-- Indices de la tabla `venta`
--
ALTER TABLE `venta`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `articulo`
--
ALTER TABLE `articulo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de la tabla `categoria`
--
ALTER TABLE `categoria`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `proveedor`
--
ALTER TABLE `proveedor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `idusuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `venta`
--
ALTER TABLE `venta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `articulo`
--
ALTER TABLE `articulo`
  ADD CONSTRAINT `articulo_ibfk_1` FOREIGN KEY (`categoria`) REFERENCES `categoria` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_cat_id` FOREIGN KEY (`categoria`) REFERENCES `categoria` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `detallesventa`
--
ALTER TABLE `detallesventa`
  ADD CONSTRAINT `detallesventa_ibfk_1` FOREIGN KEY (`idVenta`) REFERENCES `venta` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `detallesventa_ibfk_2` FOREIGN KEY (`idArticulo`) REFERENCES `articulo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
