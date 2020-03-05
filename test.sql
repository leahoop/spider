CREATE Database python;

USE python;

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for v2ex
-- ----------------------------
DROP TABLE IF EXISTS `v2ex`;
CREATE TABLE `v2ex` (
  `id` int(8) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `hot` int(5) DEFAULT '0',
  `created_on` timestamp default CURRENT_TIMESTAMP not null comment '创建时间',
  `updated_on` timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP comment '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=650147 DEFAULT CHARSET=utf8mb4;
