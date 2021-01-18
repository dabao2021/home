/*
Navicat MySQL Data Transfer

Source Server         : 本地root@mysql
Source Server Version : 50722
Source Host           : localhost:3306
Source Database       : blog

Target Server Type    : MYSQL
Target Server Version : 50722
File Encoding         : 65001

Date: 2021-01-18 23:00:18
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `article`
-- ----------------------------
DROP TABLE IF EXISTS `article`;
CREATE TABLE `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(30) NOT NULL,
  `content` longtext NOT NULL,
  `sort` int(11) NOT NULL,
  `click_num` int(11) NOT NULL,
  `zuozhe_id` int(11) DEFAULT NULL,
  `check_status` int(11) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `desc` longtext NOT NULL,
  `is_recommend` tinyint(1) NOT NULL,
  `image` longtext NOT NULL,
  `tagInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `article_zuozhe_id_ff172121_fk_zuozhe_id` (`zuozhe_id`),
  KEY `article_category_id_99127861_fk_category_id` (`category_id`),
  KEY `article_tagInfo_id_79c70551_fk_taginfo_id` (`tagInfo_id`),
  CONSTRAINT `article_category_id_99127861_fk_category_id` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`),
  CONSTRAINT `article_ibfk_1` FOREIGN KEY (`zuozhe_id`) REFERENCES `zuozhe` (`id`),
  CONSTRAINT `article_tagInfo_id_79c70551_fk_taginfo_id` FOREIGN KEY (`tagInfo_id`) REFERENCES `taginfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of article
-- ----------------------------
INSERT INTO `article` VALUES ('2', '文章题目2222', '内容222', '4', '10', '2', '1', '2021-01-05 15:08:26.188196', '2021-01-05 15:35:56.751467', '1', '22222222222', '1', 'static/images/timg.jpg', '1');
INSERT INTO `article` VALUES ('3', '文章题目3', '内容333', '1', '24', '2', '2', '2021-01-05 15:08:26.188196', '2021-01-05 15:35:53.121235', '2', '333333', '0', 'static/images/timg.jpg', '2');
INSERT INTO `article` VALUES ('4', '文章题目4', '内容4水电费水电费', '2', '5', '3', '1', '2021-01-05 15:08:26.188196', '2021-01-05 15:25:21.326393', '3', '444444', '1', 'static/images/timg.jpg', '1');
INSERT INTO `article` VALUES ('5', '文章题目5', '发的啥地方舒服舒服', '12', '1', '3', '1', '2021-01-05 15:17:24.127456', '2021-01-11 09:24:47.685873', '4', '55555555', '0', 'static/images/timg.jpg', '3');

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_ibfk_1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_ibfk_2` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_ibfk_1` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('14', 'Can view group', '3', 'view_group');
INSERT INTO `auth_permission` VALUES ('15', 'Can view permission', '2', 'view_permission');
INSERT INTO `auth_permission` VALUES ('16', 'Can view user', '4', 'view_user');
INSERT INTO `auth_permission` VALUES ('17', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('18', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('20', 'Can view content type', '5', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('21', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('22', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('24', 'Can view session', '6', 'view_session');
INSERT INTO `auth_permission` VALUES ('25', 'Can add Bookmark', '7', 'add_bookmark');
INSERT INTO `auth_permission` VALUES ('26', 'Can change Bookmark', '7', 'change_bookmark');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete Bookmark', '7', 'delete_bookmark');
INSERT INTO `auth_permission` VALUES ('28', 'Can add User Setting', '8', 'add_usersettings');
INSERT INTO `auth_permission` VALUES ('29', 'Can change User Setting', '8', 'change_usersettings');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete User Setting', '8', 'delete_usersettings');
INSERT INTO `auth_permission` VALUES ('31', 'Can add User Widget', '9', 'add_userwidget');
INSERT INTO `auth_permission` VALUES ('32', 'Can change User Widget', '9', 'change_userwidget');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete User Widget', '9', 'delete_userwidget');
INSERT INTO `auth_permission` VALUES ('34', 'Can add log entry', '10', 'add_log');
INSERT INTO `auth_permission` VALUES ('35', 'Can change log entry', '10', 'change_log');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete log entry', '10', 'delete_log');
INSERT INTO `auth_permission` VALUES ('37', 'Can view Bookmark', '7', 'view_bookmark');
INSERT INTO `auth_permission` VALUES ('38', 'Can view log entry', '10', 'view_log');
INSERT INTO `auth_permission` VALUES ('39', 'Can view User Setting', '8', 'view_usersettings');
INSERT INTO `auth_permission` VALUES ('40', 'Can view User Widget', '9', 'view_userwidget');
INSERT INTO `auth_permission` VALUES ('41', 'Can add 文章管理', '11', 'add_article');
INSERT INTO `auth_permission` VALUES ('42', 'Can change 文章管理', '11', 'change_article');
INSERT INTO `auth_permission` VALUES ('43', 'Can delete 文章管理', '11', 'delete_article');
INSERT INTO `auth_permission` VALUES ('44', 'Can add 作者', '12', 'add_zuozhe');
INSERT INTO `auth_permission` VALUES ('45', 'Can change 作者', '12', 'change_zuozhe');
INSERT INTO `auth_permission` VALUES ('46', 'Can delete 作者', '12', 'delete_zuozhe');
INSERT INTO `auth_permission` VALUES ('47', 'Can view 文章管理', '11', 'view_article');
INSERT INTO `auth_permission` VALUES ('48', 'Can view 作者', '12', 'view_zuozhe');
INSERT INTO `auth_permission` VALUES ('49', 'Can add 轮播图', '13', 'add_pic');
INSERT INTO `auth_permission` VALUES ('50', 'Can change 轮播图', '13', 'change_pic');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete 轮播图', '13', 'delete_pic');
INSERT INTO `auth_permission` VALUES ('52', 'Can view 轮播图', '13', 'view_pic');
INSERT INTO `auth_permission` VALUES ('53', 'Can add 类别', '14', 'add_category');
INSERT INTO `auth_permission` VALUES ('54', 'Can change 类别', '14', 'change_category');
INSERT INTO `auth_permission` VALUES ('55', 'Can delete 类别', '14', 'delete_category');
INSERT INTO `auth_permission` VALUES ('56', 'Can view 类别', '14', 'view_category');
INSERT INTO `auth_permission` VALUES ('57', 'Can add 标签', '15', 'add_taginfo');
INSERT INTO `auth_permission` VALUES ('58', 'Can change 标签', '15', 'change_taginfo');
INSERT INTO `auth_permission` VALUES ('59', 'Can delete 标签', '15', 'delete_taginfo');
INSERT INTO `auth_permission` VALUES ('60', 'Can view 标签', '15', 'view_taginfo');

-- ----------------------------
-- Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$36000$PcnVOkIXqmf3$H74o1W3g8AmjKvvk+NB1DQfZQ1x1kGsZYUDyMTZ37eU=', '2021-01-11 03:14:53.574873', '1', 'xadmin', '', '', '', '1', '1', '2021-01-05 13:02:38.273769');

-- ----------------------------
-- Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_ibfk_1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `category`
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(15) NOT NULL,
  `add_time` datetime(6) DEFAULT NULL,
  `path_name` varchar(15) NOT NULL,
  `is_tab` tinyint(1) NOT NULL,
  `title` varchar(15) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of category
-- ----------------------------
INSERT INTO `category` VALUES ('1', 'python', '2021-01-11 07:54:15.197873', 'python', '1', 'python学习笔记');
INSERT INTO `category` VALUES ('2', 'django', '2021-01-11 07:54:48.179873', 'django', '1', 'django学习笔记');
INSERT INTO `category` VALUES ('3', 'github', '2021-01-11 08:26:46.989873', 'github', '1', 'github学习笔记');
INSERT INTO `category` VALUES ('4', 'python爬虫', '2021-01-11 08:28:59.540873', 'python_pa', '1', 'django题目');
INSERT INTO `category` VALUES ('5', 'linux学习', '2021-01-14 14:48:44.790875', 'linux', '1', 'linux学习');

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_ibfk_1` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('11', 'users', 'article');
INSERT INTO `django_content_type` VALUES ('14', 'users', 'category');
INSERT INTO `django_content_type` VALUES ('13', 'users', 'pic');
INSERT INTO `django_content_type` VALUES ('15', 'users', 'taginfo');
INSERT INTO `django_content_type` VALUES ('12', 'users', 'zuozhe');
INSERT INTO `django_content_type` VALUES ('7', 'xadmin', 'bookmark');
INSERT INTO `django_content_type` VALUES ('10', 'xadmin', 'log');
INSERT INTO `django_content_type` VALUES ('8', 'xadmin', 'usersettings');
INSERT INTO `django_content_type` VALUES ('9', 'xadmin', 'userwidget');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2021-01-05 12:56:40.467476');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2021-01-05 12:56:41.360538');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2021-01-05 12:56:41.538435');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2021-01-05 12:56:41.552428');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2021-01-05 12:56:41.784294');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2021-01-05 12:56:41.861252');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2021-01-05 12:56:41.947203');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2021-01-05 12:56:41.961194');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2021-01-05 12:56:42.035150');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2021-01-05 12:56:42.042146');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2021-01-05 12:56:42.066133');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0008_alter_user_username_max_length', '2021-01-05 12:56:42.154101');
INSERT INTO `django_migrations` VALUES ('13', 'sessions', '0001_initial', '2021-01-05 12:56:42.218913');
INSERT INTO `django_migrations` VALUES ('14', 'users', '0001_initial', '2021-01-05 12:56:42.399809');
INSERT INTO `django_migrations` VALUES ('15', 'xadmin', '0001_initial', '2021-01-05 12:56:42.886531');
INSERT INTO `django_migrations` VALUES ('16', 'xadmin', '0002_log', '2021-01-05 12:56:43.081418');
INSERT INTO `django_migrations` VALUES ('17', 'xadmin', '0003_auto_20160715_0100', '2021-01-05 12:56:43.174364');
INSERT INTO `django_migrations` VALUES ('18', 'users', '0002_auto_20210105_2306', '2021-01-05 15:08:26.581970');
INSERT INTO `django_migrations` VALUES ('19', 'users', '0003_auto_20210105_2316', '2021-01-05 15:16:15.976934');
INSERT INTO `django_migrations` VALUES ('20', 'users', '0004_auto_20210105_2320', '2021-01-05 15:20:47.209518');
INSERT INTO `django_migrations` VALUES ('21', 'users', '0005_article_update_time', '2021-01-05 15:24:09.984470');
INSERT INTO `django_migrations` VALUES ('22', 'users', '0006_auto_20210109_2206', '2021-01-09 14:06:24.530696');
INSERT INTO `django_migrations` VALUES ('23', 'users', '0007_pic', '2021-01-09 14:22:10.909837');
INSERT INTO `django_migrations` VALUES ('24', 'users', '0008_category', '2021-01-09 15:10:59.257856');
INSERT INTO `django_migrations` VALUES ('25', 'users', '0009_auto_20210109_2339', '2021-01-09 15:39:37.705555');
INSERT INTO `django_migrations` VALUES ('26', 'users', '0010_pic_modify_time', '2021-01-09 15:52:52.702808');
INSERT INTO `django_migrations` VALUES ('27', 'users', '0011_auto_20210111_1659', '2021-01-11 09:00:12.509873');
INSERT INTO `django_migrations` VALUES ('28', 'users', '0012_auto_20210111_2215', '2021-01-11 14:15:57.494644');
INSERT INTO `django_migrations` VALUES ('29', 'users', '0013_taginfo', '2021-01-14 14:09:32.204613');
INSERT INTO `django_migrations` VALUES ('30', 'users', '0014_article_taginfo', '2021-01-18 14:31:38.741081');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('cp7c52ojs51uhokaij781dtz4wk0b45v', 'Njg3ZTdlNTZlMTQ3ZDVjMDdhMzViZTA0NjEyN2U5YjhlYzFhOWMzNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhNGM5MTQ5NWM3MDUxNDQxNzQ2OWJmNzMwZGM2Y2ZiZGYzZmNiYTc3IiwiTElTVF9RVUVSWSI6W1sidXNlcnMiLCJhcnRpY2xlIl0sIiJdfQ==', '2021-01-25 09:28:01.316873');
INSERT INTO `django_session` VALUES ('ctjxloubpi22ojb212sci5bxqradejum', 'Njg3ZTdlNTZlMTQ3ZDVjMDdhMzViZTA0NjEyN2U5YjhlYzFhOWMzNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhNGM5MTQ5NWM3MDUxNDQxNzQ2OWJmNzMwZGM2Y2ZiZGYzZmNiYTc3IiwiTElTVF9RVUVSWSI6W1sidXNlcnMiLCJhcnRpY2xlIl0sIiJdfQ==', '2021-01-23 01:59:41.456190');
INSERT INTO `django_session` VALUES ('wftlrvaen7k9k577mzu7zob16kc21k6d', 'MWQ1ZGNmNGEzNGJiYzQ5Mjg4N2Q2ZDU2ZDlhNDIzNmFhMzk0OTIzNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhNGM5MTQ5NWM3MDUxNDQxNzQ2OWJmNzMwZGM2Y2ZiZGYzZmNiYTc3IiwiTElTVF9RVUVSWSI6W1sidXNlcnMiLCJ0YWdpbmZvIl0sIiJdfQ==', '2021-01-28 15:49:46.437029');

-- ----------------------------
-- Table structure for `roll_pic`
-- ----------------------------
DROP TABLE IF EXISTS `roll_pic`;
CREATE TABLE `roll_pic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pic_name` varchar(15) NOT NULL,
  `xuhao` int(11) NOT NULL,
  `pic_path` longtext,
  `create_time` datetime(6) DEFAULT NULL,
  `modify_time` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of roll_pic
-- ----------------------------
INSERT INTO `roll_pic` VALUES ('1', 'python', '3', 'static/images/202008102025.jpg', null, '2021-01-09 17:26:52.476628');
INSERT INTO `roll_pic` VALUES ('2', 'github', '2', 'static/images/202008122338.jpg', '2021-01-09 15:56:38.236659', '2021-01-09 15:59:46.544490');
INSERT INTO `roll_pic` VALUES ('3', 'tornado', '1', 'static/images/202008122347.jpg', '2021-01-09 16:02:02.296497', '2021-01-09 17:26:59.244743');

-- ----------------------------
-- Table structure for `taginfo`
-- ----------------------------
DROP TABLE IF EXISTS `taginfo`;
CREATE TABLE `taginfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(15) NOT NULL,
  `add_time` datetime(6) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `taginfo_category_id_b7810fa8_fk_category_id` (`category_id`),
  CONSTRAINT `taginfo_category_id_b7810fa8_fk_category_id` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of taginfo
-- ----------------------------
INSERT INTO `taginfo` VALUES ('1', 'python', '2021-01-14 14:24:58.426089', '1');
INSERT INTO `taginfo` VALUES ('2', 'django', '2021-01-14 14:25:07.162939', '2');
INSERT INTO `taginfo` VALUES ('3', 'git', '2021-01-14 14:25:50.138680', '3');
INSERT INTO `taginfo` VALUES ('4', 'python语法', '2021-01-14 14:26:25.623946', '1');
INSERT INTO `taginfo` VALUES ('5', 'xadmin', '2021-01-14 14:47:46.116428', '1');
INSERT INTO `taginfo` VALUES ('6', 'Nginx', '2021-01-14 14:49:35.513639', '5');

-- ----------------------------
-- Table structure for `xadmin_bookmark`
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_bookmark`;
CREATE TABLE `xadmin_bookmark` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL,
  `url_name` varchar(64) NOT NULL,
  `query` varchar(1000) NOT NULL,
  `is_share` tinyint(1) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_bookmark_content_type_id_60941679_fk_django_co` (`content_type_id`),
  KEY `xadmin_bookmark_user_id_42d307fc_fk_auth_user_id` (`user_id`),
  CONSTRAINT `xadmin_bookmark_ibfk_1` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_bookmark_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xadmin_bookmark
-- ----------------------------

-- ----------------------------
-- Table structure for `xadmin_log`
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_log`;
CREATE TABLE `xadmin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `ip_addr` char(39) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` varchar(32) NOT NULL,
  `message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` (`content_type_id`),
  KEY `xadmin_log_user_id_bb16a176_fk_auth_user_id` (`user_id`),
  CONSTRAINT `xadmin_log_ibfk_1` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_log_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xadmin_log
-- ----------------------------
INSERT INTO `xadmin_log` VALUES ('1', '2021-01-05 13:05:01.585515', '127.0.0.1', '1', '文章题目1', 'create', '已添加。', '11', '1');
INSERT INTO `xadmin_log` VALUES ('2', '2021-01-05 13:05:32.453231', '127.0.0.1', '2', '文章题目2', 'create', '已添加。', '11', '1');
INSERT INTO `xadmin_log` VALUES ('3', '2021-01-05 13:08:14.508125', '127.0.0.1', '2', '文章题目2', 'change', '修改 zuozhe', '11', '1');
INSERT INTO `xadmin_log` VALUES ('4', '2021-01-05 13:28:29.542815', '127.0.0.1', '3', '文章题目3', 'create', '已添加。', '11', '1');
INSERT INTO `xadmin_log` VALUES ('5', '2021-01-05 13:28:52.681725', '127.0.0.1', '4', '文章题目4', 'create', '已添加。', '11', '1');
INSERT INTO `xadmin_log` VALUES ('6', '2021-01-05 13:37:29.883801', '127.0.0.1', '3', '赵六', 'create', '已添加。', '12', '1');
INSERT INTO `xadmin_log` VALUES ('7', '2021-01-05 15:17:24.129461', '127.0.0.1', '5', '文章题目5', 'create', '已添加。', '11', '1');
INSERT INTO `xadmin_log` VALUES ('8', '2021-01-09 15:56:38.239656', '127.0.0.1', '2', 'git', 'create', '已添加。', '13', '1');
INSERT INTO `xadmin_log` VALUES ('9', '2021-01-09 16:02:02.300494', '127.0.0.1', '3', 'tornado', 'create', '已添加。', '13', '1');
INSERT INTO `xadmin_log` VALUES ('10', '2021-01-11 07:54:15.221873', '127.0.0.1', '1', 'python学习', 'create', '已添加。', '14', '1');
INSERT INTO `xadmin_log` VALUES ('11', '2021-01-11 07:54:48.183873', '127.0.0.1', '2', 'django学习', 'create', '已添加。', '14', '1');
INSERT INTO `xadmin_log` VALUES ('12', '2021-01-11 08:26:46.992873', '127.0.0.1', '3', 'github', 'create', '已添加。', '14', '1');
INSERT INTO `xadmin_log` VALUES ('13', '2021-01-11 08:28:59.541873', '127.0.0.1', '4', 'python爬虫', 'create', '已添加。', '14', '1');
INSERT INTO `xadmin_log` VALUES ('14', '2021-01-14 14:24:58.432083', '127.0.0.1', '1', 'python', 'create', '已添加。', '15', '1');
INSERT INTO `xadmin_log` VALUES ('15', '2021-01-14 14:25:07.169290', '127.0.0.1', '2', 'django', 'create', '已添加。', '15', '1');
INSERT INTO `xadmin_log` VALUES ('16', '2021-01-14 14:25:50.142146', '127.0.0.1', '3', 'git', 'create', '已添加。', '15', '1');
INSERT INTO `xadmin_log` VALUES ('17', '2021-01-14 14:26:25.625950', '127.0.0.1', '4', 'python语法', 'create', '已添加。', '15', '1');
INSERT INTO `xadmin_log` VALUES ('18', '2021-01-14 14:47:46.120425', '127.0.0.1', '5', 'xadmin', 'create', '已添加。', '15', '1');
INSERT INTO `xadmin_log` VALUES ('19', '2021-01-14 14:48:44.793803', '127.0.0.1', '5', 'linux学习', 'create', '已添加。', '14', '1');
INSERT INTO `xadmin_log` VALUES ('20', '2021-01-14 14:49:35.516636', '127.0.0.1', '6', 'Nginx', 'create', '已添加。', '15', '1');

-- ----------------------------
-- Table structure for `xadmin_usersettings`
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_usersettings`;
CREATE TABLE `xadmin_usersettings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(256) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_usersettings_user_id_edeabe4a_fk_auth_user_id` (`user_id`),
  CONSTRAINT `xadmin_usersettings_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xadmin_usersettings
-- ----------------------------
INSERT INTO `xadmin_usersettings` VALUES ('1', 'dashboard:home:pos', '', '1');

-- ----------------------------
-- Table structure for `xadmin_userwidget`
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_userwidget`;
CREATE TABLE `xadmin_userwidget` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` varchar(256) NOT NULL,
  `widget_type` varchar(50) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_userwidget_user_id_c159233a_fk_auth_user_id` (`user_id`),
  CONSTRAINT `xadmin_userwidget_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xadmin_userwidget
-- ----------------------------

-- ----------------------------
-- Table structure for `zuozhe`
-- ----------------------------
DROP TABLE IF EXISTS `zuozhe`;
CREATE TABLE `zuozhe` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `zuozheNo` varchar(15) NOT NULL,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zuozhe
-- ----------------------------
INSERT INTO `zuozhe` VALUES ('1', '10001', '张三');
INSERT INTO `zuozhe` VALUES ('2', '10002', '李四');
INSERT INTO `zuozhe` VALUES ('3', '10003', '赵六');
