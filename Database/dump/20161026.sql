-- phpMyAdmin SQL Dump
-- version 4.2.12deb2+deb8u1build0.15.04.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 20, 2016 at 10:19 AM
-- Server version: 5.6.28-0ubuntu0.15.04.1
-- PHP Version: 5.6.4-4ubuntu6.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `climmobv3`
--

-- --------------------------------------------------------

--
-- Table structure for table `activitylog`
--

CREATE TABLE IF NOT EXISTS `activitylog` (
`log_id` int(9) NOT NULL,
  `log_user` varchar(80) NOT NULL,
  `log_datetime` datetime DEFAULT NULL,
  `log_type` varchar(3) DEFAULT NULL,
  `log_message` text
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `activitylog`
--

INSERT INTO `activitylog` (`log_id`, `log_user`, `log_datetime`, `log_type`, `log_message`) VALUES
(1, 'brandonmadriz', '2016-06-27 08:37:56', 'PRF', 'Bienvenido a Climmob'),
(2, 'bioversity', '2016-06-27 08:42:15', 'PRF', 'Bienvenido a Climmob'),
(3, 'kaue.desousa', '2016-10-12 10:43:58', 'PRF', 'Welcome to Climmob');

-- --------------------------------------------------------

--
-- Table structure for table `apilog`
--

CREATE TABLE IF NOT EXISTS `apilog` (
`log_id` int(9) NOT NULL,
  `log_datetime` datetime DEFAULT NULL,
  `log_ip` varchar(45) DEFAULT NULL,
  `log_user` varchar(80) NOT NULL,
  `log_uuid` varchar(80) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `assessment`
--

CREATE TABLE IF NOT EXISTS `assessment` (
  `user_name` varchar(80) NOT NULL,
  `project_cod` varchar(80) NOT NULL,
  `question_id` int(11) NOT NULL,
  `section_user` varchar(80) NOT NULL,
  `section_project` varchar(80) NOT NULL,
  `section_id` int(11) NOT NULL,
  `question_order` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `assessment`
--

INSERT INTO `assessment` (`user_name`, `project_cod`, `question_id`, `section_user`, `section_project`, `section_id`, `question_order`) VALUES
('brandonmadriz', 'Nueva prueba', 8, 'brandonmadriz', 'Nueva prueba', 2, 5),
('brandonmadriz', 'Nueva prueba', 12, 'brandonmadriz', 'Nueva prueba', 2, 4),
('brandonmadriz', 'Nueva prueba', 23, 'brandonmadriz', 'Nueva prueba', 2, 1),
('brandonmadriz', 'Nueva prueba', 27, 'brandonmadriz', 'Nueva prueba', 2, 2),
('brandonmadriz', 'Nueva prueba', 29, 'brandonmadriz', 'Nueva prueba', 2, 3);

-- --------------------------------------------------------

--
-- Table structure for table `asssection`
--

CREATE TABLE IF NOT EXISTS `asssection` (
  `user_name` varchar(80) NOT NULL,
  `project_cod` varchar(80) NOT NULL,
  `section_id` int(11) NOT NULL,
  `section_name` varchar(120) DEFAULT NULL,
  `section_content` text,
  `section_order` int(11) DEFAULT NULL,
  `section_color` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `asssection`
--

INSERT INTO `asssection` (`user_name`, `project_cod`, `section_id`, `section_name`, `section_content`, `section_order`, `section_color`) VALUES
('brandonmadriz', 'Nueva prueba', 1, 'Preguntas de ClimMob', 'Nos permiten tener la información necesaria para el analisis', 1, '#4643E8'),
('brandonmadriz', 'Nueva prueba', 2, 'Variables extras', 'Solo para mejorar los resultados', 2, '#449d44');

-- --------------------------------------------------------

--
-- Table structure for table `country`
--

CREATE TABLE IF NOT EXISTS `country` (
  `cnty_cod` varchar(3) NOT NULL,
  `cnty_name` varchar(120) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `country`
--

INSERT INTO `country` (`cnty_cod`, `cnty_name`) VALUES
('AD', 'Andorra'),
('AE', 'United Arab Emirates'),
('AF', 'Afghanistan'),
('AG', 'Antigua and Barbuda'),
('AI', 'Anguilla'),
('AL', 'Albania'),
('AM', 'Armenia'),
('AO', 'Angola'),
('AQ', 'Antarctica'),
('AR', 'Argentina'),
('AS', 'American Samoa'),
('AT', 'Austria'),
('AU', 'Australia'),
('AW', 'Aruba'),
('AX', 'Åland Islands'),
('AZ', 'Azerbaijan'),
('BA', 'Bosnia and Herzegovina'),
('BB', 'Barbados'),
('BD', 'Bangladesh'),
('BE', 'Belgium'),
('BF', 'Burkina Faso'),
('BG', 'Bulgaria'),
('BH', 'Bahrain'),
('BI', 'Burundi'),
('BJ', 'Benin'),
('BL', 'Saint Barthélemy'),
('BM', 'Bermuda'),
('BN', 'Brunei Darussalam'),
('BO', 'Bolivia'),
('BQ', 'Caribbean Netherlands '),
('BR', 'Brazil'),
('BS', 'Bahamas'),
('BT', 'Bhutan'),
('BV', 'Bouvet Island'),
('BW', 'Botswana'),
('BY', 'Belarus'),
('BZ', 'Belize'),
('CA', 'Canada'),
('CC', 'Cocos (Keeling) Islands'),
('CD', 'Congo, Democratic Republic of'),
('CF', 'Central African Republic'),
('CG', 'Congo'),
('CH', 'Switzerland'),
('CI', 'Côte d''Ivoire'),
('CK', 'Cook Islands'),
('CL', 'Chile'),
('CM', 'Cameroon'),
('CN', 'China'),
('CO', 'Colombia'),
('CR', 'Costa Rica'),
('CU', 'Cuba'),
('CV', 'Cape Verde'),
('CW', 'Curaçao'),
('CX', 'Christmas Island'),
('CY', 'Cyprus'),
('CZ', 'Czech Republic'),
('DE', 'Germany'),
('DJ', 'Djibouti'),
('DK', 'Denmark'),
('DM', 'Dominica'),
('DO', 'Dominican Republic'),
('DZ', 'Algeria'),
('EC', 'Ecuador'),
('EE', 'Estonia'),
('EG', 'Egypt'),
('EH', 'Western Sahara'),
('ER', 'Eritrea'),
('ES', 'Spain'),
('ET', 'Ethiopia'),
('FI', 'Finland'),
('FJ', 'Fiji'),
('FK', 'Falkland Islands'),
('FM', 'Micronesia, Federated States of'),
('FO', 'Faroe Islands'),
('FR', 'France'),
('GA', 'Gabon'),
('GB', 'United Kingdom'),
('GD', 'Grenada'),
('GE', 'Georgia'),
('GF', 'French Guiana'),
('GG', 'Guernsey'),
('GH', 'Ghana'),
('GI', 'Gibraltar'),
('GL', 'Greenland'),
('GM', 'Gambia'),
('GN', 'Guinea'),
('GP', 'Guadeloupe'),
('GQ', 'Equatorial Guinea'),
('GR', 'Greece'),
('GS', 'South Georgia and the South Sandwich Islands'),
('GT', 'Guatemala'),
('GU', 'Guam'),
('GW', 'Guinea-Bissau'),
('GY', 'Guyana'),
('HK', 'Hong Kong'),
('HM', 'Heard and McDonald Islands'),
('HN', 'Honduras'),
('HR', 'Croatia'),
('HT', 'Haiti'),
('HU', 'Hungary'),
('ID', 'Indonesia'),
('IE', 'Ireland'),
('IL', 'Israel'),
('IM', 'Isle of Man'),
('IN', 'India'),
('IO', 'British Indian Ocean Territory'),
('IQ', 'Iraq'),
('IR', 'Iran'),
('IS', 'Iceland'),
('IT', 'Italy'),
('JE', 'Jersey'),
('JM', 'Jamaica'),
('JO', 'Jordan'),
('JP', 'Japan'),
('KE', 'Kenya'),
('KG', 'Kyrgyzstan'),
('KH', 'Cambodia'),
('KI', 'Kiribati'),
('KM', 'Comoros'),
('KN', 'Saint Kitts and Nevis'),
('KP', 'North Korea'),
('KR', 'South Korea'),
('KW', 'Kuwait'),
('KY', 'Cayman Islands'),
('KZ', 'Kazakhstan'),
('LA', 'Lao People''s Democratic Republic'),
('LB', 'Lebanon'),
('LC', 'Saint Lucia'),
('LI', 'Liechtenstein'),
('LK', 'Sri Lanka'),
('LR', 'Liberia'),
('LS', 'Lesotho'),
('LT', 'Lithuania'),
('LU', 'Luxembourg'),
('LV', 'Latvia'),
('LY', 'Libya'),
('MA', 'Morocco'),
('MC', 'Monaco'),
('MD', 'Moldova'),
('ME', 'Montenegro'),
('MF', 'Saint-Martin (France)'),
('MG', 'Madagascar'),
('MH', 'Marshall Islands'),
('MK', 'Macedonia'),
('ML', 'Mali'),
('MM', 'Myanmar'),
('MN', 'Mongolia'),
('MO', 'Macau'),
('MP', 'Northern Mariana Islands'),
('MQ', 'Martinique'),
('MR', 'Mauritania'),
('MS', 'Montserrat'),
('MT', 'Malta'),
('MU', 'Mauritius'),
('MV', 'Maldives'),
('MW', 'Malawi'),
('MX', 'Mexico'),
('MY', 'Malaysia'),
('MZ', 'Mozambique'),
('NA', 'Namibia'),
('NC', 'New Caledonia'),
('NE', 'Niger'),
('NF', 'Norfolk Island'),
('NG', 'Nigeria'),
('NI', 'Nicaragua'),
('NL', 'The Netherlands'),
('NO', 'Norway'),
('NP', 'Nepal'),
('NR', 'Nauru'),
('NU', 'Niue'),
('NZ', 'New Zealand'),
('OM', 'Oman'),
('PA', 'Panama'),
('PE', 'Peru'),
('PF', 'French Polynesia'),
('PG', 'Papua New Guinea'),
('PH', 'Philippines'),
('PK', 'Pakistan'),
('PL', 'Poland'),
('PM', 'St. Pierre and Miquelon'),
('PN', 'Pitcairn'),
('PR', 'Puerto Rico'),
('PS', 'Palestine, State of'),
('PT', 'Portugal'),
('PW', 'Palau'),
('PY', 'Paraguay'),
('QA', 'Qatar'),
('RE', 'Réunion'),
('RO', 'Romania'),
('RS', 'Serbia'),
('RU', 'Russian Federation'),
('RW', 'Rwanda'),
('SA', 'Saudi Arabia'),
('SB', 'Solomon Islands'),
('SC', 'Seychelles'),
('SD', 'Sudan'),
('SE', 'Sweden'),
('SG', 'Singapore'),
('SH', 'Saint Helena'),
('SI', 'Slovenia'),
('SJ', 'Svalbard and Jan Mayen Islands'),
('SK', 'Slovakia'),
('SL', 'Sierra Leone'),
('SM', 'San Marino'),
('SN', 'Senegal'),
('SO', 'Somalia'),
('SR', 'Suriname'),
('SS', 'South Sudan'),
('ST', 'Sao Tome and Principe'),
('SV', 'El Salvador'),
('SX', 'Sint Maarten (Dutch part)'),
('SY', 'Syria'),
('SZ', 'Swaziland'),
('TC', 'Turks and Caicos Islands'),
('TD', 'Chad'),
('TF', 'French Southern Territories'),
('TG', 'Togo'),
('TH', 'Thailand'),
('TJ', 'Tajikistan'),
('TK', 'Tokelau'),
('TL', 'Timor-Leste'),
('TM', 'Turkmenistan'),
('TN', 'Tunisia'),
('TO', 'Tonga'),
('TR', 'Turkey'),
('TT', 'Trinidad and Tobago'),
('TV', 'Tuvalu'),
('TW', 'Taiwan'),
('TZ', 'Tanzania'),
('UA', 'Ukraine'),
('UG', 'Uganda'),
('UM', 'United States Minor Outlying Islands'),
('US', 'United States'),
('UY', 'Uruguay'),
('UZ', 'Uzbekistan'),
('VA', 'Vatican'),
('VC', 'Saint Vincent and the Grenadines'),
('VE', 'Venezuela'),
('VG', 'Virgin Islands (British)'),
('VI', 'Virgin Islands (U.S.)'),
('VN', 'Vietnam'),
('VU', 'Vanuatu'),
('WF', 'Wallis and Futuna Islands'),
('WS', 'Samoa'),
('YE', 'Yemen'),
('YT', 'Mayotte'),
('ZA', 'South Africa'),
('ZM', 'Zambia'),
('ZW', 'Zimbabwe');

-- --------------------------------------------------------

--
-- Table structure for table `enumerator`
--

CREATE TABLE IF NOT EXISTS `enumerator` (
  `user_name` varchar(80) NOT NULL,
  `project_cod` varchar(80) NOT NULL,
  `enum_id` varchar(80) NOT NULL,
  `enum_name` varchar(120) DEFAULT NULL,
  `enum_password` varchar(80) DEFAULT NULL,
  `enum_active` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `enumerator`
--

INSERT INTO `enumerator` (`user_name`, `project_cod`, `enum_id`, `enum_name`, `enum_password`, `enum_active`) VALUES
('brandonmadriz', 'COD01', 'Mapache', 'Brandon Madriz', 'qUPcoHDaLl4/pAnqhqzrSQ==', 0),
('brandonmadriz', 'Nueva prueba', 'Mapache', 'Brandon Madriz', 'qUPcoHDaLl4/pAnqhqzrSQ==', 1);

-- --------------------------------------------------------

--
-- Table structure for table `i18n`
--

CREATE TABLE IF NOT EXISTS `i18n` (
  `lang_code` varchar(5) NOT NULL,
  `lang_name` varchar(120) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `package`
--

CREATE TABLE IF NOT EXISTS `package` (
  `user_name` varchar(80) NOT NULL,
  `project_cod` varchar(80) NOT NULL,
  `package_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `pkgcomb`
--

CREATE TABLE IF NOT EXISTS `pkgcomb` (
  `user_name` varchar(80) NOT NULL,
  `project_cod` varchar(80) NOT NULL,
  `package_id` int(11) NOT NULL,
  `comb_user` varchar(80) NOT NULL,
  `comb_project` varchar(80) NOT NULL,
  `comb_code` int(11) NOT NULL,
  `pkgcomb_code` varchar(45) DEFAULT NULL,
  `pkgcomb_image` blob
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `prjalias`
--

CREATE TABLE IF NOT EXISTS `prjalias` (
  `user_name` varchar(80) NOT NULL,
  `project_cod` varchar(80) NOT NULL,
  `tech_id` int(11) NOT NULL,
  `alias_id` int(11) NOT NULL,
  `alias_name` varchar(120) DEFAULT NULL,
  `tech_used` int(11) DEFAULT NULL,
  `alias_used` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `prjalias`
--

INSERT INTO `prjalias` (`user_name`, `project_cod`, `tech_id`, `alias_id`, `alias_name`, `tech_used`, `alias_used`) VALUES
('brandonmadriz', 'COD01', 3, 1, '', 3, 13),
('brandonmadriz', 'COD01', 3, 2, '', 3, 14),
('brandonmadriz', 'COD01', 3, 3, '', 3, 11);

-- --------------------------------------------------------

--
-- Table structure for table `prjcnty`
--

CREATE TABLE IF NOT EXISTS `prjcnty` (
  `user_name` varchar(80) NOT NULL,
  `project_cod` varchar(80) NOT NULL,
  `cnty_cod` varchar(3) NOT NULL,
  `cnty_contact` varchar(120) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `prjcnty`
--

INSERT INTO `prjcnty` (`user_name`, `project_cod`, `cnty_cod`, `cnty_contact`) VALUES
('brandonmadriz', 'COD01', 'CR', 'Luis Allen');

-- --------------------------------------------------------

--
-- Table structure for table `prjcombdet`
--

CREATE TABLE IF NOT EXISTS `prjcombdet` (
  `prjcomb_user` varchar(80) NOT NULL,
  `prjcomb_project` varchar(80) NOT NULL,
  `comb_code` int(11) NOT NULL,
  `user_name` varchar(80) NOT NULL,
  `project_cod` varchar(80) NOT NULL,
  `tech_id` int(11) NOT NULL,
  `alias_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `prjcombination`
--

CREATE TABLE IF NOT EXISTS `prjcombination` (
  `user_name` varchar(80) NOT NULL,
  `project_cod` varchar(80) NOT NULL,
  `comb_code` int(11) NOT NULL,
  `comb_usable` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `prjlang`
--

CREATE TABLE IF NOT EXISTS `prjlang` (
  `user_name` varchar(80) NOT NULL,
  `project_cod` varchar(80) NOT NULL,
  `lang_code` varchar(5) NOT NULL,
  `lang_default` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `prjtech`
--

CREATE TABLE IF NOT EXISTS `prjtech` (
  `user_name` varchar(80) NOT NULL,
  `project_cod` varchar(80) NOT NULL,
  `tech_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `prjtech`
--

INSERT INTO `prjtech` (`user_name`, `project_cod`, `tech_id`) VALUES
('brandonmadriz', 'COD01', 2),
('brandonmadriz', 'COD01', 3),
('brandonmadriz', 'Nueva prueba', 4);

-- --------------------------------------------------------

--
-- Table structure for table `project`
--

CREATE TABLE IF NOT EXISTS `project` (
  `user_name` varchar(80) NOT NULL,
  `project_cod` varchar(80) NOT NULL,
  `project_name` varchar(120) DEFAULT NULL,
  `project_abstract` text,
  `project_tags` text,
  `project_pi` varchar(120) DEFAULT NULL,
  `project_piemail` varchar(120) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `project`
--

INSERT INTO `project` (`user_name`, `project_cod`, `project_name`, `project_abstract`, `project_tags`, `project_pi`, `project_piemail`) VALUES
('brandonmadriz', 'COD01', 'Frijolitos Mundiales', 'Este es el proyecto que yo tengo como base para realizar mis pruebas.', 'Solo pruebas~Vamos bien~Frijolitos', 'Brandon Madriz', 'bran3994@gmail.com'),
('brandonmadriz', 'COD02', 'Proyecto numero dos', 'Prueba para saber si el id del orden de los grupos esta bien', 'a~s~d', 'Brandon Madriz', 'bran3994@gmail.com'),
('brandonmadriz', 'Nueva prueba', 'Brandon', 'Proyecto casi generado de inmediato', 'prueba~automatico', 'Brandon Madriz', 'bran3994@gmail.com'),
('kaue.desousa', 'pruebaK', 'pruebaK', 'Probando encuesta inventario forestal', '', 'Kaue de Sousa', 'kaue.desousa@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `qstoption`
--

CREATE TABLE IF NOT EXISTS `qstoption` (
  `question_id` int(11) NOT NULL,
  `value_code` int(11) NOT NULL,
  `value_desc` varchar(120) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `qstoption`
--

INSERT INTO `qstoption` (`question_id`, `value_code`, `value_desc`) VALUES
(6, 1, 'Mas fuerte'),
(6, 2, 'Normal'),
(6, 3, 'Mas debil'),
(23, 1, 'Masculino'),
(23, 2, 'Femenino'),
(27, 1, 'Si'),
(27, 2, 'No'),
(29, 1, 'Riego'),
(29, 2, 'Fertilizantes'),
(29, 3, 'Metodos de siembra'),
(29, 4, 'Maquinarias'),
(39, 1, 'DAP'),
(39, 2, 'CAP'),
(44, 1, 'sano'),
(44, 2, 'enfermo'),
(44, 3, 'muerto'),
(45, 1, 'Opt1'),
(45, 2, 'Opt2'),
(45, 3, 'Opt3'),
(45, 4, 'Opt4');

-- --------------------------------------------------------

--
-- Table structure for table `qstprjopt`
--

CREATE TABLE IF NOT EXISTS `qstprjopt` (
  `project_user` varchar(80) NOT NULL,
  `project_cod` varchar(80) NOT NULL,
  `question_id` int(11) NOT NULL,
  `value_code` int(11) NOT NULL,
  `value_desc` varchar(120) DEFAULT NULL,
  `parent_user` varchar(80) DEFAULT NULL,
  `parent_project` varchar(80) DEFAULT NULL,
  `parent_question` int(11) DEFAULT NULL,
  `parent_value` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `question`
--

CREATE TABLE IF NOT EXISTS `question` (
`question_id` int(11) NOT NULL,
  `question_desc` varchar(120) DEFAULT NULL,
  `question_notes` text,
  `question_unit` varchar(120) DEFAULT NULL,
  `question_dtype` int(11) DEFAULT NULL COMMENT 'Can also be Producer input, producer select, package select, enumerator select',
  `question_oth` int(11) DEFAULT NULL,
  `question_cmp` varchar(120) DEFAULT NULL,
  `question_reqinreg` tinyint(4) DEFAULT '0',
  `question_reqinasses` tinyint(4) DEFAULT '0',
  `question_optperprj` tinyint(4) DEFAULT '0',
  `parent_question` int(11) DEFAULT NULL,
  `user_name` varchar(80) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `question`
--

INSERT INTO `question` (`question_id`, `question_desc`, `question_notes`, `question_unit`, `question_dtype`, `question_oth`, `question_cmp`, `question_reqinreg`, `question_reqinasses`, `question_optperprj`, `parent_question`, `user_name`) VALUES
(4, 'Nombre del observador', 'Consulta sobre el nombre del participante que realiza el ensayo, se utiliza para dar seguimiento al mismo.', 'Nombre completo de la persona a cargo del ensayo', 1, 0, '', 1, 0, 0, NULL, 'bioversity'),
(6, 'Epoca de lluvia', 'Saber que tal fueron las condiciones lluviosas para la epoca de siembra', 'Seleccione la que más se llevo acabo', 5, 1, '', 0, 0, 0, NULL, 'brandonmadriz'),
(8, 'Calidad de consumo', 'Los facilitadores consultaran a los observadores cual les parece mejor para el consumo.', 'Los observadores tuvieron que haber probado el frijol', 1, 0, '', 0, 0, 0, NULL, 'brandonmadriz'),
(10, 'Punto GPS de la finca', 'Esta pregunta es muy importante si deseamos utilizar mapas en el futuro.', 'Debe de estar ubicado en la entrada de la finca', 4, 0, '', 1, 0, 0, NULL, 'bioversity'),
(12, 'Telefono', 'Esta diseñada para tener el contacto del observador, para la recolección de información.', 'Puede ser telefono fijo o celular', 3, 0, '', 0, 0, 0, NULL, 'bioversity'),
(13, 'Nombre del familiar', 'Tener una referencia de un familiar en caso de no encontrar a el observador', 'Puede ser el padre, la madre, esposa o esposo', 1, 0, '', 1, 0, 0, NULL, 'bioversity'),
(14, 'Pueblo', 'Pueblo en el que habita el observador', '', 1, 0, '', 1, 0, 0, NULL, 'bioversity'),
(15, 'Region', 'Region donde vive el observador', '', 1, 0, '', 1, 0, 0, NULL, 'bioversity'),
(16, 'Edad', 'Indicar la edad del observador', '', 3, 0, '', 1, 0, 0, NULL, 'bioversity'),
(23, 'Genero', 'Saber el genero del observador', 'Esto no es una pregunta, solo marque la opción correspondiente', 5, 0, '', 1, 0, 0, NULL, 'bioversity'),
(24, 'Código de paquete', 'Asignar un código a un observador el cual posee la tecnologías que deberá utilizar en el ensayo.', 'Verifique que sea el código que esta seleccionando este correcto', 7, 0, '', 1, 0, 0, NULL, 'bioversity'),
(27, 'Ha hecho uso de riego en el ensayo ?', 'Saber si el observador uso riego durante el proceso de EPM.', 'Consultar al observador', 5, 0, '', 0, 0, 0, NULL, 'brandonmadriz'),
(29, 'Que aplico durante el desarrollo del ensayo ?', 'Saber que tecnologias utilizan los productores durante el ensayo', 'Puede marcar varias', 6, 0, '', 0, 0, 0, NULL, 'brandonmadriz'),
(30, 'Region 2', 'nada', 'Escriba la region', 1, 0, '', 1, 0, 0, NULL, 'bioversity'),
(31, 'Area finca', 'Area de la finca en ha', 'El area de la finca es expresada en hectareas', 2, 0, '', 0, 0, 0, NULL, 'kaue.desousa'),
(32, 'Area parcela', 'Area de la parcela en ha', 'El area de la parcela es expresada en hectareas', 2, 0, '', 0, 0, 0, NULL, 'kaue.desousa'),
(33, 'Punto GPS parcela', 'Debe estar ubicado en un punto central en la parcela', '', 4, 0, '', 0, 0, 0, NULL, 'kaue.desousa'),
(34, 'Pendiente', 'Pendiente del terreno de la parcela', 'Debe estar indicado en porcentaje', 2, 0, '', 0, 0, 0, NULL, 'kaue.desousa'),
(35, 'ID arbol', 'El numero de identificacion del arbol en la parcela', '', 1, 0, '', 0, 0, 0, NULL, 'kaue.desousa'),
(36, 'Especie', 'Nombre de la especie', '', 1, 0, '', 0, 0, 0, NULL, 'kaue.desousa'),
(37, 'GPS arbol', 'Punto de GPS del arbol ', '', 4, 0, '', 0, 0, 0, NULL, 'kaue.desousa'),
(38, 'Base DAP/CAP', 'El DAP (diametro) o CAP del arbol a 1.3m del suelo', 'debe estar en centimetros', 2, 0, '', 0, 0, 0, NULL, 'kaue.desousa'),
(39, 'DAP/CAP', 'Si la informacion tomada anteriormente era DAP o CAP', '', 5, 0, '', 0, 0, 0, NULL, 'kaue.desousa'),
(40, 'Altura total', 'Estimacion de la altura total del arbol', 'La altura total se toma de la base del arbol hasta la ultima rama', 2, 0, '', 0, 0, 0, NULL, 'kaue.desousa'),
(41, 'Altura comercial', 'Altura comercial del arbol', 'La altura total se toma de la base del arbol la primera rama en el fuste', 2, 0, '', 0, 0, 0, NULL, 'kaue.desousa'),
(42, 'Diametro copa 1', 'Diametro de la copa del arbol, primera medicion', 'Se mide en metros', 2, 0, '', 0, 0, 0, NULL, 'kaue.desousa'),
(43, 'Diametro copa 2', 'Segunda medicion del diametro de copa', 'Se mide en metros', 2, 0, '', 0, 0, 0, NULL, 'kaue.desousa'),
(44, 'Sanidad', 'Estado fitossanitario del arbol', 'seleccionar una opcion', 5, 0, '', 0, 0, 0, NULL, 'kaue.desousa'),
(45, 'Multiple selection', 'Multiple selection', '', 6, 1, '', 0, 0, 0, NULL, 'kaue.desousa');

-- --------------------------------------------------------

--
-- Table structure for table `registry`
--

CREATE TABLE IF NOT EXISTS `registry` (
  `user_name` varchar(80) NOT NULL,
  `project_cod` varchar(80) NOT NULL,
  `question_id` int(11) NOT NULL,
  `section_user` varchar(80) DEFAULT NULL,
  `section_project` varchar(80) DEFAULT NULL,
  `section_id` int(11) DEFAULT NULL,
  `question_order` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `registry`
--

INSERT INTO `registry` (`user_name`, `project_cod`, `question_id`, `section_user`, `section_project`, `section_id`, `question_order`) VALUES
('brandonmadriz', 'COD01', 4, 'brandonmadriz', 'COD01', 2, 1),
('brandonmadriz', 'COD01', 8, 'brandonmadriz', 'COD01', 3, 3),
('brandonmadriz', 'COD01', 10, 'brandonmadriz', 'COD01', 2, 2),
('brandonmadriz', 'Nueva prueba', 4, 'brandonmadriz', 'Nueva prueba', 1, 1),
('brandonmadriz', 'Nueva prueba', 6, 'brandonmadriz', 'Nueva prueba', 3, 1),
('brandonmadriz', 'Nueva prueba', 10, 'brandonmadriz', 'Nueva prueba', 2, 2),
('brandonmadriz', 'Nueva prueba', 12, 'brandonmadriz', 'Nueva prueba', 1, 8),
('brandonmadriz', 'Nueva prueba', 13, 'brandonmadriz', 'Nueva prueba', 1, 2),
('brandonmadriz', 'Nueva prueba', 14, 'brandonmadriz', 'Nueva prueba', 1, 6),
('brandonmadriz', 'Nueva prueba', 15, 'brandonmadriz', 'Nueva prueba', 1, 7),
('brandonmadriz', 'Nueva prueba', 16, 'brandonmadriz', 'Nueva prueba', 1, 4),
('brandonmadriz', 'Nueva prueba', 23, 'brandonmadriz', 'Nueva prueba', 1, 3),
('brandonmadriz', 'Nueva prueba', 24, 'brandonmadriz', 'Nueva prueba', 1, 5),
('brandonmadriz', 'Nueva prueba', 30, 'brandonmadriz', 'Nueva prueba', 3, 2),
('kaue.desousa', 'pruebaK', 4, 'kaue.desousa', 'pruebaK', 2, 1),
('kaue.desousa', 'pruebaK', 35, 'kaue.desousa', 'pruebaK', 1, 3),
('kaue.desousa', 'pruebaK', 36, 'kaue.desousa', 'pruebaK', 1, 4),
('kaue.desousa', 'pruebaK', 37, 'kaue.desousa', 'pruebaK', 2, 2),
('kaue.desousa', 'pruebaK', 38, 'kaue.desousa', 'pruebaK', 3, 1),
('kaue.desousa', 'pruebaK', 39, 'kaue.desousa', 'pruebaK', 3, 2),
('kaue.desousa', 'pruebaK', 40, 'kaue.desousa', 'pruebaK', 4, 1),
('kaue.desousa', 'pruebaK', 41, 'kaue.desousa', 'pruebaK', 4, 2),
('kaue.desousa', 'pruebaK', 42, 'kaue.desousa', 'pruebaK', 5, 1),
('kaue.desousa', 'pruebaK', 43, 'kaue.desousa', 'pruebaK', 5, 2),
('kaue.desousa', 'pruebaK', 44, 'kaue.desousa', 'pruebaK', 5, 3),
('kaue.desousa', 'pruebaK', 45, 'kaue.desousa', 'pruebaK', 5, 4);

-- --------------------------------------------------------

--
-- Table structure for table `regsection`
--

CREATE TABLE IF NOT EXISTS `regsection` (
  `user_name` varchar(80) NOT NULL,
  `project_cod` varchar(80) NOT NULL,
  `section_id` int(11) NOT NULL,
  `section_name` varchar(45) DEFAULT NULL,
  `section_content` text,
  `section_order` int(11) DEFAULT NULL,
  `section_color` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Registry section / Seccion en registro';

--
-- Dumping data for table `regsection`
--

INSERT INTO `regsection` (`user_name`, `project_cod`, `section_id`, `section_name`, `section_content`, `section_order`, `section_color`) VALUES
('brandonmadriz', 'COD01', 2, 'Información personal', 'Saber cual es la informacion personal de los observadores, que nos permitan indentificarlos durante el proceso', 1, '#449d44'),
('brandonmadriz', 'COD01', 3, 'Variables explicativas', 'Tener algunos indicadores.', 2, '#BB0CE8'),
('brandonmadriz', 'Nueva prueba', 1, 'Base', 'Basic unit ClimMob', 2, '#4643E8'),
('brandonmadriz', 'Nueva prueba', 2, 'Detalles de la finca', 'Separar los detalles de la persona con los de la finca', 1, '#449d44'),
('brandonmadriz', 'Nueva prueba', 3, 'Variables explicativas', 'solo prueba', 3, '#BB0CE8'),
('kaue.desousa', 'pruebaK', 1, 'Arbol', 'Basic unit ClimMob', 2, '#4643E8'),
('kaue.desousa', 'pruebaK', 2, 'Introduction', 'basic information', 1, '#449d44'),
('kaue.desousa', 'pruebaK', 3, 'DBH', 'diameter at the breast height', 3, '#BB0CE8'),
('kaue.desousa', 'pruebaK', 4, 'Height', 'heigth measures', 4, '#E8640C'),
('kaue.desousa', 'pruebaK', 5, 'Other', 'other', 5, '#17AAFF');

-- --------------------------------------------------------

--
-- Table structure for table `sector`
--

CREATE TABLE IF NOT EXISTS `sector` (
`sector_cod` int(11) NOT NULL,
  `sector_name` varchar(120) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `sector`
--

INSERT INTO `sector` (`sector_cod`, `sector_name`) VALUES
(1, 'Bioversity International\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `techalias`
--

CREATE TABLE IF NOT EXISTS `techalias` (
  `tech_id` int(11) NOT NULL,
  `alias_id` int(11) NOT NULL,
  `alias_name` varchar(120) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `techalias`
--

INSERT INTO `techalias` (`tech_id`, `alias_id`, `alias_name`) VALUES
(2, 6, 'Maiz uno'),
(2, 7, 'Maiz dos'),
(2, 8, 'Maiz tres'),
(2, 9, 'Maiz cuatro'),
(2, 10, 'Maiz cinco'),
(3, 11, 'Metabenzotiazuron'),
(3, 12, 'Bentazon'),
(3, 13, 'Pendimetalina'),
(3, 14, 'Fluazifop-butil'),
(3, 15, 'Paraquat'),
(3, 16, 'Glifosato'),
(4, 17, 'cacao 1'),
(4, 18, 'cacao 2'),
(6, 19, 'Amadeus 77'),
(6, 20, 'Bayo'),
(6, 21, 'Vaina Blanca'),
(7, 22, 'Extender'),
(7, 23, 'Tendergreen'),
(7, 24, 'Contender '),
(7, 25, 'Guaria'),
(8, 26, 'Ortega');

-- --------------------------------------------------------

--
-- Table structure for table `technology`
--

CREATE TABLE IF NOT EXISTS `technology` (
`tech_id` int(11) NOT NULL,
  `tech_name` varchar(45) DEFAULT NULL,
  `user_name` varchar(80) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `technology`
--

INSERT INTO `technology` (`tech_id`, `tech_name`, `user_name`) VALUES
(2, 'Maiz', 'bioversity'),
(3, 'Fertilizantes', 'brandonmadriz'),
(4, 'Cacao', 'brandonmadriz'),
(6, 'Frijol', 'brandonmadriz'),
(7, 'Vainica', 'brandonmadriz'),
(8, 'Tomate', 'brandonmadriz'),
(9, 'as', 'brandonmadriz');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `user_name` varchar(80) NOT NULL,
  `user_fullname` varchar(120) DEFAULT NULL,
  `user_password` varchar(80) DEFAULT NULL,
  `user_organization` varchar(120) DEFAULT NULL,
  `user_email` varchar(120) DEFAULT NULL,
  `user_apikey` varchar(45) DEFAULT NULL,
  `user_about` text,
  `user_cnty` varchar(3) NOT NULL,
  `user_sector` int(11) NOT NULL,
  `user_active` tinyint(4) DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='User table: Store the users';

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_name`, `user_fullname`, `user_password`, `user_organization`, `user_email`, `user_apikey`, `user_about`, `user_cnty`, `user_sector`, `user_active`) VALUES
('bioversity', 'Bioversity', '5dY2k6Z2rwqAtwQ7z/dS6g==', 'Bioversity International', 'International', '20abbf14-841a-4ae2-bc4f-5c0c051b2d8e', '', 'CR', 1, 1),
('brandonmadriz', 'Brandon Madriz Araya', 'Lygc89R57qtLM2TCKW7QlA==', 'Bioversity International', 'bran1016@hotmail.com', '11ca7937-5b69-416e-a024-541b9532a657', '', 'CR', 1, 1),
('kaue.desousa', 'Kaue de Sousa', 'q7WWu/2cJBJxA4K8EsQLKw==', 'Bioversity International', 'kaue.desousa@catie.ac.cr', 'f009ef5a-533b-4355-a20e-1253304ed98b', '', 'CR', 1, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `activitylog`
--
ALTER TABLE `activitylog`
 ADD PRIMARY KEY (`log_id`), ADD KEY `fk_activitylog_user1_idx` (`log_user`);

--
-- Indexes for table `apilog`
--
ALTER TABLE `apilog`
 ADD PRIMARY KEY (`log_id`), ADD KEY `fk_apilog_user1_idx` (`log_user`);

--
-- Indexes for table `assessment`
--
ALTER TABLE `assessment`
 ADD PRIMARY KEY (`user_name`,`project_cod`,`question_id`), ADD KEY `fk_assessment_question1_idx` (`question_id`), ADD KEY `fk_assessment_asssection1_idx` (`section_user`,`section_project`,`section_id`);

--
-- Indexes for table `asssection`
--
ALTER TABLE `asssection`
 ADD PRIMARY KEY (`user_name`,`project_cod`,`section_id`);

--
-- Indexes for table `country`
--
ALTER TABLE `country`
 ADD PRIMARY KEY (`cnty_cod`);

--
-- Indexes for table `enumerator`
--
ALTER TABLE `enumerator`
 ADD PRIMARY KEY (`user_name`,`project_cod`,`enum_id`);

--
-- Indexes for table `i18n`
--
ALTER TABLE `i18n`
 ADD PRIMARY KEY (`lang_code`);

--
-- Indexes for table `package`
--
ALTER TABLE `package`
 ADD PRIMARY KEY (`user_name`,`project_cod`,`package_id`);

--
-- Indexes for table `pkgcomb`
--
ALTER TABLE `pkgcomb`
 ADD PRIMARY KEY (`user_name`,`project_cod`,`package_id`,`comb_user`,`comb_project`,`comb_code`), ADD KEY `fk_pkgcomb_prjcombination1_idx` (`comb_user`,`comb_project`,`comb_code`);

--
-- Indexes for table `prjalias`
--
ALTER TABLE `prjalias`
 ADD PRIMARY KEY (`user_name`,`project_cod`,`tech_id`,`alias_id`), ADD KEY `fk_prjalias_prjtech1_idx` (`user_name`,`project_cod`,`tech_id`), ADD KEY `fk_prjalias_techalias1_idx` (`tech_used`,`alias_used`);

--
-- Indexes for table `prjcnty`
--
ALTER TABLE `prjcnty`
 ADD PRIMARY KEY (`user_name`,`project_cod`,`cnty_cod`), ADD KEY `fk_prjcnty_country1_idx` (`cnty_cod`);

--
-- Indexes for table `prjcombdet`
--
ALTER TABLE `prjcombdet`
 ADD PRIMARY KEY (`prjcomb_user`,`prjcomb_project`,`comb_code`,`user_name`,`project_cod`,`tech_id`,`alias_id`), ADD KEY `fk_prjcombdet_prjalias1_idx` (`user_name`,`project_cod`,`tech_id`,`alias_id`);

--
-- Indexes for table `prjcombination`
--
ALTER TABLE `prjcombination`
 ADD PRIMARY KEY (`user_name`,`project_cod`,`comb_code`);

--
-- Indexes for table `prjlang`
--
ALTER TABLE `prjlang`
 ADD PRIMARY KEY (`user_name`,`project_cod`,`lang_code`), ADD KEY `fk_prjlang_i18n1_idx` (`lang_code`);

--
-- Indexes for table `prjtech`
--
ALTER TABLE `prjtech`
 ADD PRIMARY KEY (`user_name`,`project_cod`,`tech_id`), ADD KEY `fk_prjtech_technology1_idx` (`tech_id`);

--
-- Indexes for table `project`
--
ALTER TABLE `project`
 ADD PRIMARY KEY (`user_name`,`project_cod`), ADD KEY `fk_project_user1_idx` (`user_name`);

--
-- Indexes for table `qstoption`
--
ALTER TABLE `qstoption`
 ADD PRIMARY KEY (`question_id`,`value_code`);

--
-- Indexes for table `qstprjopt`
--
ALTER TABLE `qstprjopt`
 ADD PRIMARY KEY (`project_user`,`project_cod`,`question_id`,`value_code`), ADD KEY `fk_qstprjopt_question1_idx` (`question_id`), ADD KEY `fk_qstprjopt_qstprjopt1_idx` (`parent_user`,`parent_project`,`parent_question`,`parent_value`);

--
-- Indexes for table `question`
--
ALTER TABLE `question`
 ADD PRIMARY KEY (`question_id`), ADD KEY `fk_question_user1_idx` (`user_name`), ADD KEY `fk_question_question1_idx` (`parent_question`);

--
-- Indexes for table `registry`
--
ALTER TABLE `registry`
 ADD PRIMARY KEY (`user_name`,`project_cod`,`question_id`), ADD KEY `fk_registry_question1_idx` (`question_id`), ADD KEY `fk_registry_regsection1_idx` (`section_user`,`section_project`,`section_id`);

--
-- Indexes for table `regsection`
--
ALTER TABLE `regsection`
 ADD PRIMARY KEY (`user_name`,`project_cod`,`section_id`);

--
-- Indexes for table `sector`
--
ALTER TABLE `sector`
 ADD PRIMARY KEY (`sector_cod`);

--
-- Indexes for table `techalias`
--
ALTER TABLE `techalias`
 ADD PRIMARY KEY (`tech_id`,`alias_id`), ADD KEY `fk_techalias_technology1_idx` (`tech_id`);

--
-- Indexes for table `technology`
--
ALTER TABLE `technology`
 ADD PRIMARY KEY (`tech_id`), ADD KEY `fk_crop_user1_idx` (`user_name`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
 ADD PRIMARY KEY (`user_name`), ADD KEY `fk_user_lkpcountry_idx` (`user_cnty`), ADD KEY `fk_user_lkpsector1_idx` (`user_sector`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `activitylog`
--
ALTER TABLE `activitylog`
MODIFY `log_id` int(9) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `apilog`
--
ALTER TABLE `apilog`
MODIFY `log_id` int(9) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `question`
--
ALTER TABLE `question`
MODIFY `question_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=46;
--
-- AUTO_INCREMENT for table `sector`
--
ALTER TABLE `sector`
MODIFY `sector_cod` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `technology`
--
ALTER TABLE `technology`
MODIFY `tech_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=10;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `activitylog`
--
ALTER TABLE `activitylog`
ADD CONSTRAINT `fk_activitylog_user1` FOREIGN KEY (`log_user`) REFERENCES `user` (`user_name`) ON UPDATE NO ACTION;

--
-- Constraints for table `apilog`
--
ALTER TABLE `apilog`
ADD CONSTRAINT `fk_apilog_user1` FOREIGN KEY (`log_user`) REFERENCES `user` (`user_name`) ON UPDATE NO ACTION;

--
-- Constraints for table `assessment`
--
ALTER TABLE `assessment`
ADD CONSTRAINT `fk_assessment_asssection1` FOREIGN KEY (`section_user`, `section_project`, `section_id`) REFERENCES `asssection` (`user_name`, `project_cod`, `section_id`) ON DELETE CASCADE ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_assessment_project1` FOREIGN KEY (`user_name`, `project_cod`) REFERENCES `project` (`user_name`, `project_cod`) ON DELETE CASCADE ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_assessment_question1` FOREIGN KEY (`question_id`) REFERENCES `question` (`question_id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `asssection`
--
ALTER TABLE `asssection`
ADD CONSTRAINT `fk_asssection_project1` FOREIGN KEY (`user_name`, `project_cod`) REFERENCES `project` (`user_name`, `project_cod`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `enumerator`
--
ALTER TABLE `enumerator`
ADD CONSTRAINT `fk_enumerator_project1` FOREIGN KEY (`user_name`, `project_cod`) REFERENCES `project` (`user_name`, `project_cod`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `package`
--
ALTER TABLE `package`
ADD CONSTRAINT `fk_package_project1` FOREIGN KEY (`user_name`, `project_cod`) REFERENCES `project` (`user_name`, `project_cod`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `pkgcomb`
--
ALTER TABLE `pkgcomb`
ADD CONSTRAINT `fk_pkgcomb_package1` FOREIGN KEY (`user_name`, `project_cod`, `package_id`) REFERENCES `package` (`user_name`, `project_cod`, `package_id`) ON DELETE CASCADE ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_pkgcomb_prjcombination1` FOREIGN KEY (`comb_user`, `comb_project`, `comb_code`) REFERENCES `prjcombination` (`user_name`, `project_cod`, `comb_code`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `prjalias`
--
ALTER TABLE `prjalias`
ADD CONSTRAINT `fk_prjalias_prjtech1` FOREIGN KEY (`user_name`, `project_cod`, `tech_id`) REFERENCES `prjtech` (`user_name`, `project_cod`, `tech_id`) ON DELETE CASCADE ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_prjalias_techalias1` FOREIGN KEY (`tech_used`, `alias_used`) REFERENCES `techalias` (`tech_id`, `alias_id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `prjcnty`
--
ALTER TABLE `prjcnty`
ADD CONSTRAINT `fk_prjcnty_country1` FOREIGN KEY (`cnty_cod`) REFERENCES `country` (`cnty_cod`) ON DELETE CASCADE ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_prjcnty_project1` FOREIGN KEY (`user_name`, `project_cod`) REFERENCES `project` (`user_name`, `project_cod`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `prjcombdet`
--
ALTER TABLE `prjcombdet`
ADD CONSTRAINT `fk_prjcombdet_prjalias1` FOREIGN KEY (`user_name`, `project_cod`, `tech_id`, `alias_id`) REFERENCES `prjalias` (`user_name`, `project_cod`, `tech_id`, `alias_id`) ON DELETE CASCADE ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_prjcombdet_prjcombination1` FOREIGN KEY (`prjcomb_user`, `prjcomb_project`, `comb_code`) REFERENCES `prjcombination` (`user_name`, `project_cod`, `comb_code`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `prjcombination`
--
ALTER TABLE `prjcombination`
ADD CONSTRAINT `fk_prjcombination_project1` FOREIGN KEY (`user_name`, `project_cod`) REFERENCES `project` (`user_name`, `project_cod`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `prjlang`
--
ALTER TABLE `prjlang`
ADD CONSTRAINT `fk_prjlang_i18n1` FOREIGN KEY (`lang_code`) REFERENCES `i18n` (`lang_code`) ON DELETE CASCADE ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_prjlang_project1` FOREIGN KEY (`user_name`, `project_cod`) REFERENCES `project` (`user_name`, `project_cod`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `prjtech`
--
ALTER TABLE `prjtech`
ADD CONSTRAINT `fk_prjtech_project1` FOREIGN KEY (`user_name`, `project_cod`) REFERENCES `project` (`user_name`, `project_cod`) ON DELETE CASCADE ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_prjtech_technology1` FOREIGN KEY (`tech_id`) REFERENCES `technology` (`tech_id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `project`
--
ALTER TABLE `project`
ADD CONSTRAINT `fk_project_user1` FOREIGN KEY (`user_name`) REFERENCES `user` (`user_name`) ON UPDATE NO ACTION;

--
-- Constraints for table `qstoption`
--
ALTER TABLE `qstoption`
ADD CONSTRAINT `fk_qstoption_question1` FOREIGN KEY (`question_id`) REFERENCES `question` (`question_id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `qstprjopt`
--
ALTER TABLE `qstprjopt`
ADD CONSTRAINT `fk_qstprjopt_project1` FOREIGN KEY (`project_user`, `project_cod`) REFERENCES `project` (`user_name`, `project_cod`) ON DELETE CASCADE ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_qstprjopt_qstprjopt1` FOREIGN KEY (`parent_user`, `parent_project`, `parent_question`, `parent_value`) REFERENCES `qstprjopt` (`project_user`, `project_cod`, `question_id`, `value_code`) ON DELETE CASCADE ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_qstprjopt_question1` FOREIGN KEY (`question_id`) REFERENCES `question` (`question_id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `question`
--
ALTER TABLE `question`
ADD CONSTRAINT `fk_question_question1` FOREIGN KEY (`parent_question`) REFERENCES `question` (`question_id`) ON DELETE CASCADE ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_question_user1` FOREIGN KEY (`user_name`) REFERENCES `user` (`user_name`) ON UPDATE NO ACTION;

--
-- Constraints for table `registry`
--
ALTER TABLE `registry`
ADD CONSTRAINT `fk_registry_project1` FOREIGN KEY (`user_name`, `project_cod`) REFERENCES `project` (`user_name`, `project_cod`) ON DELETE CASCADE ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_registry_question1` FOREIGN KEY (`question_id`) REFERENCES `question` (`question_id`) ON DELETE CASCADE ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_registry_regsection1` FOREIGN KEY (`section_user`, `section_project`, `section_id`) REFERENCES `regsection` (`user_name`, `project_cod`, `section_id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `regsection`
--
ALTER TABLE `regsection`
ADD CONSTRAINT `fk_regsection_project1` FOREIGN KEY (`user_name`, `project_cod`) REFERENCES `project` (`user_name`, `project_cod`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `techalias`
--
ALTER TABLE `techalias`
ADD CONSTRAINT `fk_techalias_technology1` FOREIGN KEY (`tech_id`) REFERENCES `technology` (`tech_id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `technology`
--
ALTER TABLE `technology`
ADD CONSTRAINT `fk_crop_user1` FOREIGN KEY (`user_name`) REFERENCES `user` (`user_name`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `user`
--
ALTER TABLE `user`
ADD CONSTRAINT `fk_user_lkpcountry` FOREIGN KEY (`user_cnty`) REFERENCES `country` (`cnty_cod`) ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_user_lkpsector1` FOREIGN KEY (`user_sector`) REFERENCES `sector` (`sector_cod`) ON UPDATE NO ACTION;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
