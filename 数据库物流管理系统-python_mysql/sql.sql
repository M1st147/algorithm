-- 创建数据库
CREATE DATABASE IF NOT EXISTS fu_logistics;

-- 使用数据库
USE fu_logistics;

-- 创建表：收件人
CREATE TABLE IF NOT EXISTS recipient (
    Rname VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    RID VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL PRIMARY KEY,
    Raddress VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    Rsex VARCHAR(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    Rphonenumber VARCHAR(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
);

-- 创建表：寄件人
CREATE TABLE IF NOT EXISTS sender (
    Sname VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    SID VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL PRIMARY KEY,
    Saddress VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    Ssex VARCHAR(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    Sphonenumber VARCHAR(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
);

-- 创建表：配送员
CREATE TABLE IF NOT EXISTS distributor (
    Dname VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    Dnum VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL PRIMARY KEY,
    DID VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    Dsex VARCHAR(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    Dphonenumber VARCHAR(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
);

-- 创建订单表
CREATE TABLE IF NOT EXISTS orders (
    Onum VARCHAR(20) NOT NULL PRIMARY KEY,
    Odelivery_time DATETIME NOT NULL DEFAULT '2023-01-01 00:00:00',
    Olog_station VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    Odistributor VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    Osender VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    Orecipient VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    Ogoods VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    Oprice DECIMAL(10, 2)
);

-- 创建表：管理员
CREATE TABLE IF NOT EXISTS manger (
    username VARCHAR(255) NOT NULL PRIMARY KEY,
    password VARCHAR(255) NOT NULL
);

-- 插入初始管理员数据
INSERT INTO manger (username, password) VALUES 
('admin', '123456'),
('user', '123456');

-- 确保表中没有重复的用户名
DELETE FROM manger
WHERE username IN (
    SELECT username
    FROM (
        SELECT username
        FROM manger
        GROUP BY username
        HAVING COUNT(*) > 1
    ) AS temp
);

-- 删除其他重复的记录（仅保留一条）
DELETE t1 FROM manger t1
INNER JOIN manger t2 
WHERE 
    t1.username = t2.username AND 
    t1.password = t2.password AND 
    t1.username > t2.username;

-- 插入初始数据：收件人，使用IGNORE忽略重复插入
INSERT IGNORE INTO recipient (Rname, RID, Raddress, Rsex, Rphonenumber) VALUES 
('rname1', 'RID123456', 'address1', 'man', '12345678901'),
('rnmae2', 'RID654321', 'address2', 'woman', '10987654321');

-- 插入初始数据：寄件人，使用IGNORE忽略重复插入
INSERT IGNORE INTO sender (Sname, SID, Saddress, Ssex, Sphonenumber) VALUES 
('sname1', 'SID123456', 'address3', 'man', '12345678902'),
('sname2', 'SID654321', 'address4', 'woman', '10987654322');

-- 插入初始数据：配送员，使用IGNORE忽略重复插入
INSERT IGNORE INTO distributor (Dname, Dnum, DID, Dsex, Dphonenumber) VALUES 
('Dname1', 'Dnum123456', 'DID123456', 'man', '12345678903'),
('Dname2', 'Dnum654321', 'DID654321', 'woman', '10987654323');

-- 插入示例数据到订单表，使用INSERT IGNORE忽略重复插入，ON DUPLICATE KEY UPDATE更新数据
INSERT IGNORE INTO orders (Onum, Odelivery_time, Olog_station, Odistributor, Osender, Orecipient, Ogoods, Oprice) VALUES
('1001', '2023-06-01 10:00:00', 'siteA', 'postman1', 'sname1', 'Rname1', 'shop1', 100.00),
('1002', '2023-06-02 11:00:00', 'site', 'postman2', 'sname2', 'Rname2', 'shop2', 200.00),
('1003', '2023-06-03 12:00:00', 'siteC', 'postman3', 'sname3', 'Rname3', 'shop3', 300.00)
ON DUPLICATE KEY UPDATE Odelivery_time = VALUES(ODelivery_time), Olog_station = VALUES(Olog_station),
Odistributor = VALUES(Odistributor), Osender = VALUES(OSender), Orecipient = VALUES(Orecipient),
Ogoods = VALUES(Ogoods), Oprice = VALUES(Oprice);

