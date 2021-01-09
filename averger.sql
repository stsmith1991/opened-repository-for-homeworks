-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Хост: sql7.freesqldatabase.com
-- Время создания: Янв 09 2021 г., 07:21
-- Версия сервера: 5.5.62-0ubuntu0.14.04.1
-- Версия PHP: 7.0.33-0ubuntu0.16.04.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `sql7384797`
--

-- --------------------------------------------------------

--
-- Структура таблицы `arhive`
--

CREATE TABLE `arhive` (
  `arvive_id` bigint(6) NOT NULL,
  `date` date NOT NULL,
  `id_source` tinyint(2) NOT NULL,
  `aver_value` float(3,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Структура таблицы `boil_types`
--

CREATE TABLE `boil_types` (
  `id` tinyint(1) NOT NULL,
  `type` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_romanian_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_romanian_ci;

--
-- Дамп данных таблицы `boil_types`
--

INSERT INTO `boil_types` VALUES(3, NULL);
INSERT INTO `boil_types` VALUES(1, 'Насыщенный');
INSERT INTO `boil_types` VALUES(2, 'Перегретый');

-- --------------------------------------------------------

--
-- Структура таблицы `cases`
--

CREATE TABLE `cases` (
  `case_id` tinyint(1) NOT NULL,
  `time` char(5) DEFAULT NULL,
  `addiction` tinytext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Дамп данных таблицы `cases`
--

INSERT INTO `cases` VALUES(1, '9:00', NULL);
INSERT INTO `cases` VALUES(2, '11:00', NULL);
INSERT INTO `cases` VALUES(3, '13:00', NULL);
INSERT INTO `cases` VALUES(4, '15:00', NULL);
INSERT INTO `cases` VALUES(5, '17:00', NULL);
INSERT INTO `cases` VALUES(6, '19:00', NULL);

-- --------------------------------------------------------

--
-- Структура таблицы `investigation`
--

CREATE TABLE `investigation` (
  `id` int(4) NOT NULL,
  `quality_criteria` varchar(15) CHARACTER SET utf8 COLLATE utf8_romanian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Дамп данных таблицы `investigation`
--

INSERT INTO `investigation` VALUES(1, 'Маслосодержание');
INSERT INTO `investigation` VALUES(2, 'Жёсткость');
INSERT INTO `investigation` VALUES(3, 'Щёлочность ф/ф');
INSERT INTO `investigation` VALUES(4, 'Полная щёлочнос');
INSERT INTO `investigation` VALUES(5, 'СО2');
INSERT INTO `investigation` VALUES(6, 'О2');
INSERT INTO `investigation` VALUES(7, 'Солесодержание');
INSERT INTO `investigation` VALUES(8, 'рН');
INSERT INTO `investigation` VALUES(9, 'Прозрачность');
INSERT INTO `investigation` VALUES(10, 'Продувка');
INSERT INTO `investigation` VALUES(11, 'Окисляемость');
INSERT INTO `investigation` VALUES(12, 'Раствор. Fe');

-- --------------------------------------------------------

--
-- Структура таблицы `meashures`
--

CREATE TABLE `meashures` (
  `meashure_id` int(4) NOT NULL,
  `id_case` tinyint(1) NOT NULL,
  `source_id` tinyint(2) NOT NULL,
  `inv_id` int(4) NOT NULL,
  `value` float DEFAULT NULL,
  `bitness` tinyint(1) DEFAULT '2',
  `id_unit` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Структура таблицы `seqtion_types`
--

CREATE TABLE `seqtion_types` (
  `id` tinyint(1) NOT NULL,
  ` type_seq` char(7) CHARACTER SET utf8 COLLATE utf8_romanian_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Дамп данных таблицы `seqtion_types`
--

INSERT INTO `seqtion_types` VALUES(3, NULL);
INSERT INTO `seqtion_types` VALUES(2, 'Солевой');
INSERT INTO `seqtion_types` VALUES(1, 'Чистый');

-- --------------------------------------------------------

--
-- Структура таблицы `sources`
--

CREATE TABLE `sources` (
  `source_id` tinyint(2) NOT NULL,
  `source_title` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_romanian_ci DEFAULT NULL,
  `par_id` tinyint(1) NOT NULL,
  `seq_type_id` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Дамп данных таблицы `sources`
--

INSERT INTO `sources` VALUES(1, 'Насыщенный пар 7 котла', 1, 3);
INSERT INTO `sources` VALUES(2, 'Перегретый пар 7 котла', 2, 3);
INSERT INTO `sources` VALUES(3, 'Насыщенный пар 8 котла', 1, 3);
INSERT INTO `sources` VALUES(4, 'Перегретый пар 8 котла', 2, 3);
INSERT INTO `sources` VALUES(5, 'Насыщенный пар 9 котла', 1, 3);
INSERT INTO `sources` VALUES(6, 'Перегретый пар 9 котла', 2, 3);
INSERT INTO `sources` VALUES(7, 'Насыщенный пар 12 котла', 1, 3);
INSERT INTO `sources` VALUES(8, 'Перегретый пар 12 котла', 2, 3);
INSERT INTO `sources` VALUES(9, 'Чистый отсек 7 котла', 3, 1);
INSERT INTO `sources` VALUES(10, 'Солевой отсек 7 котла', 3, 2);
INSERT INTO `sources` VALUES(11, 'Чистый отсек 9 котла', 3, 1);
INSERT INTO `sources` VALUES(12, 'Солевой отсек 9 котла', 3, 2);
INSERT INTO `sources` VALUES(13, 'Чистый отсек 12 котла', 3, 1);
INSERT INTO `sources` VALUES(14, 'Солевой отсек 12 котла', 3, 2);
INSERT INTO `sources` VALUES(15, 'Солевой отсек 8 котла', 3, 2);
INSERT INTO `sources` VALUES(16, 'Исходная вода', 3, 3);
INSERT INTO `sources` VALUES(17, 'Осветлённая вода', 3, 3);
INSERT INTO `sources` VALUES(18, 'Вторая ступень', 3, 3);
INSERT INTO `sources` VALUES(19, 'Питательная вода', 3, 3);
INSERT INTO `sources` VALUES(20, 'Конденсат с НФ', 3, 3);
INSERT INTO `sources` VALUES(21, 'Конденсат с бойлер', 3, 3);
INSERT INTO `sources` VALUES(22, 'Исх.после 3-ки', 3, 3);
INSERT INTO `sources` VALUES(23, 'Осветл. вода(4кот.)', 3, 3);
INSERT INTO `sources` VALUES(24, 'Подпитка', 3, 3);
INSERT INTO `sources` VALUES(25, 'Подпитка паров', 3, 3);
INSERT INTO `sources` VALUES(26, 'Хим.очищ.', 3, 3);
INSERT INTO `sources` VALUES(27, 'Сет.прям.гор.', 3, 3);
INSERT INTO `sources` VALUES(28, 'Сет.обр.гор.', 3, 3);
INSERT INTO `sources` VALUES(29, 'Сет.прям.зав.', 3, 3);
INSERT INTO `sources` VALUES(30, 'Сет.обр.зав.', 3, 3);

-- --------------------------------------------------------

--
-- Структура таблицы `units`
--

CREATE TABLE `units` (
  `unit_id` tinyint(1) NOT NULL,
  `title` tinytext CHARACTER SET utf8 COLLATE utf8_romanian_ci
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Дамп данных таблицы `units`
--

INSERT INTO `units` VALUES(1, 'мг-экв/л');
INSERT INTO `units` VALUES(2, 'г/литр');
INSERT INTO `units` VALUES(3, NULL);
INSERT INTO `units` VALUES(4, 'см');
INSERT INTO `units` VALUES(5, 'мгО2/л');
INSERT INTO `units` VALUES(6, 'мг Fe/л');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `arhive`
--
ALTER TABLE `arhive`
  ADD PRIMARY KEY (`arvive_id`),
  ADD KEY `arhive_id_source-sources_source_id` (`id_source`);

--
-- Индексы таблицы `boil_types`
--
ALTER TABLE `boil_types`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `type` (`type`);

--
-- Индексы таблицы `cases`
--
ALTER TABLE `cases`
  ADD PRIMARY KEY (`case_id`),
  ADD UNIQUE KEY `time` (`time`);

--
-- Индексы таблицы `investigation`
--
ALTER TABLE `investigation`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `meashures`
--
ALTER TABLE `meashures`
  ADD PRIMARY KEY (`meashure_id`),
  ADD KEY `meashures_id_case-cases_case_id` (`id_case`),
  ADD KEY `meashures_source_id-sources_source_id` (`source_id`),
  ADD KEY `meashures_inv_id-investigation_id` (`inv_id`),
  ADD KEY `meashures_id_unit-units_unit_id` (`id_unit`);

--
-- Индексы таблицы `seqtion_types`
--
ALTER TABLE `seqtion_types`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY ` type_seq` (` type_seq`);

--
-- Индексы таблицы `sources`
--
ALTER TABLE `sources`
  ADD PRIMARY KEY (`source_id`),
  ADD KEY `sources_par_id-boil_types_id` (`par_id`),
  ADD KEY `sources_seq_type_id-seqtion_types_id` (`seq_type_id`);

--
-- Индексы таблицы `units`
--
ALTER TABLE `units`
  ADD PRIMARY KEY (`unit_id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `arhive`
--
ALTER TABLE `arhive`
  MODIFY `arvive_id` bigint(6) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT для таблицы `boil_types`
--
ALTER TABLE `boil_types`
  MODIFY `id` tinyint(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT для таблицы `cases`
--
ALTER TABLE `cases`
  MODIFY `case_id` tinyint(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT для таблицы `investigation`
--
ALTER TABLE `investigation`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT для таблицы `meashures`
--
ALTER TABLE `meashures`
  MODIFY `meashure_id` int(4) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT для таблицы `seqtion_types`
--
ALTER TABLE `seqtion_types`
  MODIFY `id` tinyint(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT для таблицы `units`
--
ALTER TABLE `units`
  MODIFY `unit_id` tinyint(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `arhive`
--
ALTER TABLE `arhive`
  ADD CONSTRAINT `arhive_id_source-sources_source_id` FOREIGN KEY (`id_source`) REFERENCES `sources` (`source_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `meashures`
--
ALTER TABLE `meashures`
  ADD CONSTRAINT `meashures_id_unit-units_unit_id` FOREIGN KEY (`id_unit`) REFERENCES `units` (`unit_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `meashures_id_case-cases_case_id` FOREIGN KEY (`id_case`) REFERENCES `cases` (`case_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `meashures_inv_id-investigation_id` FOREIGN KEY (`inv_id`) REFERENCES `investigation` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `meashures_source_id-sources_source_id` FOREIGN KEY (`source_id`) REFERENCES `sources` (`source_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `sources`
--
ALTER TABLE `sources`
  ADD CONSTRAINT `sources_par_id-boil_types_id` FOREIGN KEY (`par_id`) REFERENCES `boil_types` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `sources_seq_type_id-seqtion_types_id` FOREIGN KEY (`seq_type_id`) REFERENCES `seqtion_types` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
