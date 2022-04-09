/*
SQLyog Ultimate v12.4.3 (64 bit)
MySQL - 8.0.23 : Database - sesion
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`sesion` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `sesion`;

/*Table structure for table `categorias` */

DROP TABLE IF EXISTS `categorias`;

CREATE TABLE `categorias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Descripcion` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `categorias` */

/*Table structure for table `productos` */

DROP TABLE IF EXISTS `productos`;

CREATE TABLE `productos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Descripcion` varchar(255) NOT NULL,
  `Precio` float NOT NULL,
  `Estado` varchar(20) NOT NULL,
  `usuario_id` int NOT NULL,
  `categoria_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usuario_id` (`usuario_id`),
  KEY `categoria_id` (`categoria_id`),
  CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`),
  CONSTRAINT `productos_ibfk_2` FOREIGN KEY (`categoria_id`) REFERENCES `categorias` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `productos` */

/*Table structure for table `usuarios` */

DROP TABLE IF EXISTS `usuarios`;

CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) NOT NULL,
  `Descripcion` varchar(255) NOT NULL,
  `imagen` text NOT NULL,
  `Celular` varchar(50) NOT NULL,
  `Direccion` varchar(50) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `Contraseña` varchar(255) NOT NULL,
  `estado` tinyint DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `usuarios` */

insert  into `usuarios`(`id`,`Nombre`,`Descripcion`,`imagen`,`Celular`,`Direccion`,`correo`,`Contraseña`,`estado`) values 
(1,'ilver','sadga','url','56786','barrio fatima','ediililv@gmail.com','$2b$12$iAAQzYktkyGKG7LDHEIvUuiTg59zg0p3eAgRZmyj6AVr7xHz1WRrG',0),
(2,'ander','jajaj','asds','5677','barrio fatima','daza04@hotmail.com','$2b$12$ooSLc4FjLUGWn6dvVHX0C.fjB8jEEjIo8wlvNkwvVumy2cwXC7Pba',0),
(3,'sandra','jajaja','ual','876','americas','cielotovar11@gmail.com','$2b$12$gmx5Pa7Ixm8Xt6TcpLRdlemZ96us2vICw9gD6.kH86sJWHLFK5FUG',0),
(4,'darewin','zjfgjas','auisgdf','676','sdf','cielotovar11@gmail.com','$2b$12$yer5Xx.RnqE0cS2fgeM6auQdQRJKXSJommUBsWXU4lbTZIWPByGfi',0),
(5,'ilver','asfa','ur','7965','jbfak','davidvivas2020@itp.edu.co','$2b$12$46TLyT/BLmqHDrv4EHvF6.3w0KU5AK7Qh0AeN964DcR3CB1xNmj2O',0),
(6,'ilver','salsa','saf','444','sasad','ilverchapal2020@itp.edu.co','$2b$12$/crduKnrY/Ro4wmCdbDXY.oRs65iL4XjPXl.L5ahVg/nI54RVzlk2',0),
(7,'ilver','salsa','wd','56786','barrio fatima','ilverchapal2020@itp.edu.co','safewf',0),
(8,'ilver','salsa','adf','456789','barrio fatima','ilverchapal2020@itp.edu.co','Ilverand@5ja',0),
(9,'yobani','asfdasdf','afwert','45789','wfew','ilverchapal2020@itp.edu.co','Yobani@7jaj',0),
(10,'ilver','salsa','asfdsadfgg','4566879','sddhg','ilverchapal2020@itp.edu.co','b7b29955d43c25e3667dbdf75f50d9fafa274c14',0),
(11,'ilver','sdaf','129096198_2038159742990699_488192502938840004_n.jpg','56786','barrio fatima','ilverchapal2020@itp.edu.co','56bab6be278328213c686586654e9f11a9b8a06a',0),
(12,'ilver','salsa','images.jpg','45657','barrio fatima','ilverchapal2020@itp.edu.co','56bab6be278328213c686586654e9f11a9b8a06a',0);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
