from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2

Matrix = [[0,1706.7,526.4,0,1497,1136.3,1445.8,1728.3,864.4,1362.3,1443.2,1410,805.1,1031.5,781.1,1003.1,364.6,482.6,279.8,768.6,461.4,752.5,972.6,771.7,698.3,901.6,1086.9,994.2,416.7,737.5,1171.7,881.6,1052.1,1164.3,868.7,409.7,498.6,685.7,1693.3,1875.3,302.7,1297.1,1663.4,1427.8],[1614.3,0,1382.2,1614.3,2192.7,1851.9,2686.5,2995.8,2216.9,1545.3,1599.2,1550.6,1796.5,1685.3,1597.7,1518.5,1779.9,2033.2,1891.8,2295.5,2009.6,2279.4,2054.5,2040.4,1235.2,1249.6,1290.2,2433.5,1943.6,1074.2,1128.2,1229.6,1192.7,823.3,1106.1,1440.2,1528.1,2100.8,2357.4,2757.6,1586.5,1676.3,1929.1,1681.3],[534.8,1446.5,0,534.8,1885.4,1473.2,1834.2,2011.5,1252.8,1549,1561.5,1622,1094.3,1131.5,895.5,1103.1,656.3,871,738.7,1051.8,765.9,1035.7,1160.9,960,798.3,1047.8,1205.2,1277.4,699.9,476.7,877.2,999.9,1264.1,891.6,534.2,196.5,356.2,874,1881.6,2063.6,342.8,1448.6,1851.7,1566.8],[0,1706.7,526.4,0,1497,1136.3,1445.8,1728.3,864.4,1362.3,1443.2,1410,805.1,1031.5,781.1,1003.1,364.6,482.6,279.8,768.6,461.4,752.5,972.6,771.7,698.3,901.6,1086.9,994.2,416.7,737.5,1171.7,881.6,1052.1,1164.3,868.7,409.7,498.6,685.7,1693.3,1875.3,302.7,1297.1,1663.4,1427.8],[1418.2,2192.4,1835.2,1418.2,0,557.7,608.1,2149,1325.3,1031.6,1615.8,1986.8,1123.8,961,1040,1085.5,1439.8,1204.8,1545.6,1530.2,1879.6,1769.1,2234.4,2150.1,1315.1,1094.9,1339.3,1874.4,1834.9,1623.6,2265.6,1275.3,1628.9,1677.3,1770.8,1718.5,1891.8,2052.1,2750.3,2966.2,1662.4,2682,2788.7,2832.4],[1096.3,1832,1437.4,1096.3,568.8,0,1062.6,1896.2,966.1,651.1,1255.4,1626.4,687,521.4,600.4,725.1,1052.8,882.9,1223.7,1209.4,1557.7,1448.3,1918,1829.3,954.7,734.5,978.9,1558,1513,1200,1863.6,914.9,1268.5,1316.9,1331.2,1396.6,1569.9,1731.3,2433.9,2649.8,1340.5,2360.1,2472.3,2510.5],[1379.1,2741.6,1796.1,1379.1,651.6,1106.9,0,1834.1,1198.5,1580.8,2140,2536,1144.1,1439.4,1262.4,1496.3,1400.7,1165.7,1495.8,1231.5,1599.7,1470.2,1919.5,1851.2,1682.6,1644.1,1888.5,1559.5,1729,1826.7,2442.7,1824.5,2178.1,2226.5,1957.9,1679.4,1852.7,1753.4,2435.4,2651.3,1623.3,2433,2473.8,2693.1],[1799.2,3111,2046.1,1799.2,2171.9,2026.5,1868,0,1242.3,2252.5,2836.7,3064,1667.2,1962.5,1785.5,2019.4,1922.9,1692.7,1687.3,1240.7,1524.3,1185.1,1224.4,1507.6,2205.7,2328.9,2545.2,895.3,1653.6,2349.8,2362.4,2407.3,2706.1,2776.6,2431.9,1925.8,1948.6,1639.8,1415.3,1631.2,1854.1,1757.2,1778.7,2017.3],[805.5,2218.4,1222.5,805.5,1296.7,925.9,1181.5,1136.6,0,1151.9,1736.1,2046.8,566.6,861.9,684.9,918.8,827.1,592.1,781,449.8,818,688.7,1158.4,1069.7,1105.1,1228.3,1444.6,798.4,947.3,1249.2,1869.1,1306.7,1688.9,1676,1380.4,1105.8,1242.3,971.7,1674.3,1890.2,1049.7,1651.3,1712.7,1911.4],[1265.8,1550.9,1515,1265.8,1025.9,685.1,1519.7,2065.7,1135.6,0,811.6,1195.2,809.5,522.1,695.6,621.5,1148,1052.4,1380.7,1378.9,1727.2,1617.8,2087.5,1998.8,878.6,658.4,559.3,1727.5,1682.5,1187.1,1829.1,639.4,837.3,1117.1,1384.6,1518.6,1691.9,1900.8,2603.4,2819.3,1462.5,2394.8,2641.8,2513],[1419.8,1573.3,1501.6,1419.8,1678.7,1342.9,2162.9,2723.5,1793.4,840.4,0,972.9,1426.5,1232.7,1183.3,1027.1,1409.9,1631.2,1556.1,2036.7,1839.6,2109.4,2234.6,2033.7,865.2,922.3,542.6,2351.1,1773.6,1213.4,1855.4,622.7,746.7,1139.5,1395.4,1540.2,1713.5,1947.7,2955.3,3137.3,1484.1,2421.1,2803.8,2539.3],[1434.8,1610.4,1634.2,1434.8,2103.8,1763,2597.6,3058.1,2128,1292.3,1016.9,0,1707.6,1596.4,1508.8,1429.6,1670.5,1853.7,1712.3,2140.5,1854.6,2124.4,2249.6,2048.7,1146.3,1160.7,1008,2366.1,1788.6,1323.9,1902.6,982.4,579.5,1176.6,1521.4,1555.2,1728.5,1962.7,2970.3,3152.3,1499.1,2468.3,2840.9,2586.5],[745.9,1760.2,1028.4,745.9,1104,685.5,1195.2,1544.9,614.8,819.7,1383.1,1588.6,0,378.9,226.7,460.6,679.1,427.3,873.3,858.1,1207.3,1097,1566.7,1478,646.9,770.1,986.4,1206.7,1162.6,791,1454.6,848.5,1230.7,1217.8,922.2,1046.2,1219.5,1380,2082.6,2298.5,990.1,2009.7,2121,2138.5],[933.5,1687.2,1052,933.5,912.5,494,1406.3,1784.3,854.2,495.6,1198.2,1481.6,328.9,0,215,309.1,667.4,659.1,900.1,1097.5,1289.3,1336.4,1777.9,1577,670.5,589.7,834.1,1446.1,1267.5,814.6,1478.2,770.1,1123.7,1172.1,945.8,1090.6,1263.9,1491,2322,2537.9,1034.5,2043.9,2360.4,2162.1],[729,1645.1,913.3,729,1034.6,616.1,1294.4,1644.1,714,715.2,1209.3,1473.5,293.6,274.4,0,286.8,462.9,447.9,695.6,957.3,1084.8,1196.2,1573.4,1372.5,531.8,596.3,812.6,1305.9,1063,675.9,1339.5,733.4,1115.6,1102.7,807.1,934.4,1107.7,1286.5,2181.8,2397.7,878.3,1897.9,2220.2,2023.4],[995.2,1489.7,1077,995.2,1008,667.2,1501.8,1901.4,971.3,591.3,994.8,1284.1,550.9,369.2,287.1,0,750,735,982.7,1214.6,1371.9,1453.5,1810,1609.1,479.2,392.2,598.1,1563.2,1349,839.6,1503.2,572.6,926.2,974.6,970.8,1115.6,1288.9,1523.1,2439.1,2655,1059.5,2068.9,2477.5,2187.1],[350.3,1818.6,639.3,350.3,1473.6,1055.1,1475.4,1824.1,894,1154.2,1439.7,1530.2,732.6,713.4,463,749.8,0,471.9,283.8,863.5,673,885.7,1161.6,960.7,676.5,939.6,1083.4,1127.4,651.2,849.4,1285.9,878.1,1172.3,1276.2,980.6,522.6,695.9,874.7,1882.3,2064.3,466.5,1486.1,1852.4,1636.5],[437.4,2042,854.4,437.4,1269.3,908.6,1218.1,1566.8,636.7,1134.6,1649.8,1745.3,433.7,696.7,440.5,727.3,459,0,564.8,880,898.8,1118.9,1376.7,1175.8,971.8,1036.8,1253.1,1228.6,854.1,1072.8,1501,1173.4,1387.4,1499.6,1204,737.7,911,1089.8,2097.4,2279.4,681.6,1701.2,2067.5,1851.6],[279.5,1914.6,746.3,279.5,1579.2,1218.5,1506.8,1619,804.6,1401,1593.4,1617.9,887.3,960.2,709.8,996.6,291.3,564.8,0,621,410.3,643.2,1112.5,911.6,830.2,1093.3,1237.1,884.9,367.4,945.4,1392.9,1031.8,1260,1372.2,1076.6,629.6,693.7,765.7,1833.2,2015.2,536.1,1410.3,1803.3,1528.5],[800.2,2348.7,1050.6,800.2,1567.8,1294.7,1285.3,1226.6,510.5,1520.7,2101.7,2068.5,935.4,1230.7,1053.7,1287.6,874.2,932.8,638.6,0,512.4,442.6,1064.1,823.6,1356.8,1560.1,1745.4,684.3,658.1,1378.9,1670,1540.1,1710.6,1793.8,1436.4,930.3,953.1,725.6,1719.6,1901.6,858.6,1405.2,1689.7,1665.3],[407.8,2014.3,716.2,407.8,1813.5,1472.5,1531,1409.4,756.2,1698.5,1767.3,1734.1,1141.3,1274,1023.6,1310.4,605.1,818.8,323.7,450,0,433.6,881.3,680.4,1022.4,1225.7,1411,675.3,210.4,1044.5,1335.6,1205.7,1376.2,1459.4,1102,595.9,618.7,526.2,1602,1784,524.2,1205.8,1572.1,1453.5],[855.1,2395.3,1102,855.1,1798.4,1525.3,1515.9,1173.4,741.1,1751.3,2153.1,2119.9,1166,1461.3,1284.3,1518.2,978.8,1191.5,743.2,477.1,580.2,0,701.1,460.6,1408.2,1611.5,1796.8,439.3,709.5,1430.3,1646.7,1591.5,1762,1845.2,1487.8,981.7,1004.5,548.2,1474.6,1656.6,910,1057.4,1444.7,1317.5],[902.1,2028.4,1133.3,902.1,2345.6,1984.9,2055.1,1189.6,1266.5,2169.2,2184.4,2151.2,1653.7,1772.7,1536.7,1744.3,1151.1,1331.2,1061.6,1047,850.5,702.5,0,407.3,1439.5,1642.8,1828.1,510.1,784.2,1461.6,1279.8,1622.8,1793.3,1876.5,1519.1,1013,1115.7,539.5,904,1086,956.9,636.9,874.1,897],[746.1,2102,977.3,746.1,2147.9,1828.9,1865.4,1456.3,1090.6,2013.2,2028.4,1995.2,1497.7,1616.7,1380.7,1588.3,995.1,1175.2,905.6,826.6,694.5,448.6,347,0,1283.5,1486.8,1672.1,792.2,628.2,1305.6,1353.4,1466.8,1637.3,1720.5,1363.1,857,934.6,301.2,1170.7,1352.7,800.9,764.1,1140.8,1024.2],[714,1295.8,795.8,714,1312.1,971.3,1721.5,2071.2,1141.1,885.7,898.2,1089.2,720.7,733.5,521.9,485.6,704.1,969.8,850.3,1384.4,1133.8,1403.6,1528.8,1327.9,0,369,541.9,1645.3,1067.8,558.4,1222,336.6,731.3,780.7,689.6,834.4,1007.7,1241.9,2249.5,2431.5,778.3,1787.7,2198.3,1905.9],[927.4,1285.1,1044.2,927.4,1067,726.2,1560.8,2152.6,1222.5,650.3,929.6,1079.5,812.8,559.6,549,392.8,952.5,996.9,1098.7,1465.8,1347.2,1617,1742.2,1541.3,402.3,0,573.3,1814.4,1281.2,716.3,1358.3,368,721.6,770,913.8,1047.8,1221.1,1455.3,2462.9,2644.9,991.7,1924,2334.6,2042.2],[1066.9,1288.4,1148.7,1066.9,1353.6,1012.8,1847.4,2393.4,1463.3,510.3,522.8,932.7,1073.6,866.8,816.7,660.5,1057,1264.6,1203.2,1706.6,1486.7,1756.5,1881.7,1680.8,512.3,569.4,0,1998.2,1420.7,860.5,1502.5,269.8,571.2,854.6,1042.5,1187.3,1360.6,1594.8,2602.4,2784.4,1131.2,2068.2,2478.8,2186.4],[1033.9,2497.8,1280.8,1033.9,1937.1,1628.8,1633.2,906.4,844.6,1854.8,2331.9,2298.7,1269.5,1564.8,1387.8,1621.7,1157.6,1295,922,655.9,759,419.8,553.1,800.8,1587,1790.3,1975.6,0,888.3,1609.1,1749.2,1770.3,1940.8,2024,1666.6,1160.5,1183.3,888.4,1207.6,1389.6,1088.8,1106.3,1177.7,1366.4],[434.2,1998.9,700.8,434.2,1859.6,1498.9,1676.6,1555,901.8,1724.9,1751.9,1718.7,1167.7,1300.4,1050,1311.8,631.5,845.2,350.1,595.3,261.3,579.2,855.8,654.9,1007,1210.3,1395.6,820.9,0,1029.1,1320.2,1190.3,1360.8,1444,1086.6,580.5,603.3,509,1576.5,1758.5,508.8,1180.3,1546.6,1438.1],[660.4,1093.1,449.6,660.4,1614.9,1241.5,1863.4,2213.1,1283,1198.2,1213.4,1273.2,862.6,899.8,663.8,871.4,877.7,1079.3,937.9,1362.9,1077,1346.8,1472,1271.1,566.6,671.8,857.1,1588.5,1011,0,841.6,651.8,915.3,538.2,276.4,507.6,681.4,1185.1,2192.7,2374.7,653.9,1407.3,1817.9,1525.5],[1074.3,1158.2,863.3,1074.3,2242.2,1861.6,2474.8,2235.8,1893.4,1797.9,1840.7,1803.2,1482.7,1519.9,1283.9,1491.5,1296.9,1511.6,1279.7,1623.1,1337.2,1590,1294.5,1280.4,1186.7,1299.1,1484.4,1673.5,1271.2,855.8,0,1279.1,1445.3,943.7,772.3,813.5,690.4,1340.8,1733.2,2031,828.6,894.3,1304.9,1012.5],[846.2,1208.6,928,846.2,1291.8,951,1785.6,2203.4,1273.3,610,622.5,915.8,852.9,784.4,654.1,617.6,836.3,1102,982.5,1516.6,1266,1535.8,1661,1460.1,291.6,348.7,266.2,1777.5,1200,639.8,1281.8,0,557.9,655.1,821.8,966.6,1139.9,1374.1,2381.7,2563.7,910.5,1847.5,2258.1,1965.7],[976.5,1152.1,1175.9,976.5,1645.5,1304.7,2139.3,2599.8,1669.7,830.6,750.3,565.6,1249.3,1138.1,1050.5,971.3,1212.2,1395.4,1254,1682.2,1396.3,1666.1,1791.3,1590.4,688,702.4,575.5,1907.8,1330.3,865.6,1444.3,561.4,0,718.3,1063.1,1096.9,1270.2,1504.4,2512,2694,1040.8,2010,2382.6,2128.2],[1080,818.6,846.2,1080,1669.1,1328.3,2162.9,2623.4,1693.3,1087.6,1141.5,1092.9,1272.9,1161.7,1074.1,994.9,1256.3,1498.9,1357.5,1759.5,1473.6,1743.4,1868.6,1667.7,711.6,726,832.5,1985.1,1407.6,538.2,972.4,665.1,732.4,0,585.3,904.2,1078,1581.7,2377,2674.8,1050.5,1538.1,1948.7,1656.3],[703.6,1085.4,451.8,703.6,1703.2,1284.7,1906.6,2256.3,1326.2,1351.3,1366.5,1426.3,905.8,943,707,914.6,920.9,1122.5,981.1,1365.1,1079.2,1349,1474.2,1273.3,609.8,824.9,1010.2,1590.7,1013.2,250.1,779.8,804.9,1068.4,586.4,0,509.8,683.6,1187.3,2184.4,2376.9,656.1,1345.5,1756.1,1463.7],[436.6,1556.1,230.2,436.6,1787.2,1426.5,1736,1903.2,1154.6,1561.8,1577,1543.8,1095.3,1165.3,929.3,1136.9,558.1,772.8,640.5,943.5,657.6,927.4,1052.6,851.7,832.1,1035.4,1220.7,1169.1,591.6,586.3,829,1015.4,1185.9,1001.2,643.8,0,238.5,765.7,1773.3,1955.3,220.9,1377.1,1743.4,1500.4],[492.4,1695,348.7,492.4,1946,1585.3,1894.8,1999.7,1313.4,1720.6,1735.8,1702.6,1254.1,1324.1,1088.1,1295.7,716.9,931.6,697.8,1040,754.1,1023.9,1142,918.1,990.9,1194.2,1379.5,1265.6,688.1,732.7,827.2,1174.2,1344.7,1147.6,790.2,227.3,0,855.1,1862.7,2044.7,241.1,1237.1,1647.7,1355.3],[614.6,2143.9,845.8,614.6,2002.1,1697.4,1719.6,1598,944.8,1881.7,1896.9,1863.7,1366.2,1485.2,1249.2,1456.8,863.6,1043.7,713.4,680.8,484.2,584.9,551.3,310.8,1152,1355.3,1540.6,863.9,436,1174.1,1406.6,1335.3,1505.8,1589,1231.6,725.5,828.2,0,1334.4,1516.4,669.4,900.9,1304.5,1161],[1677.7,2333.7,1908.9,1677.7,2805.5,2497.2,2501.6,1345.9,1713,2723.2,2960,2926.8,2137.9,2433.2,2256.2,2490.1,1926.7,2106.8,1837.2,1717.5,1626.1,1481.4,945.3,1182.9,2215.1,2418.4,2603.7,1191.6,1559.8,2209.4,1673.1,2398.4,2568.9,2297.3,2125.9,1788.6,1891.3,1315.1,0,630,1732.5,874,604.7,1053.3],[1884,2890.3,2115.2,1884,3030.5,2722.2,2726.6,1570.9,1938,2948.2,3166.3,3133.1,2362.9,2658.2,2481.2,2715.1,2133,2313.1,2043.5,1923.8,1832.4,1687.7,1151.6,1389.2,2421.4,2624.7,2810,1397.9,1766.1,2443.5,2156,2604.7,2775.2,2753.2,2501,1994.9,2097.6,1521.4,732.6,0,1938.8,1430.6,1161.3,1609.9],[310.5,1654.5,356.4,310.5,1718.8,1358.1,1667.6,1834.8,1086.2,1493.4,1508.6,1475.4,1026.9,1096.9,860.9,1068.5,489.7,704.4,538.1,875.1,589.2,859,984.2,783.3,763.7,967,1152.3,1100.7,523.2,684.7,901.1,947,1117.5,1099.6,742.2,195,244.2,697.3,1704.9,1886.9,0,1308.7,1675,1452.6],[1233.7,1726.5,1422.2,1233.7,2677.2,2316.5,2414.6,1702.1,1639.8,2402.6,2445.4,2407.9,1985.3,2104.3,1868.3,2075.9,1482.7,1662.8,1393.2,1375.8,1182.1,997.8,690.8,688.2,1771.1,1903.8,2089.1,1095.2,1115.8,1460.5,951.2,1883.8,2050,1548.4,1377,1335.7,1205.8,837.3,948.4,1348.6,1285.8,0,520.1,358.8],[1656.1,2007.2,1844.6,1656.1,2935.8,2627.5,2631.9,1766.4,1843.3,2775.1,2829,2780.4,2268.2,2526.7,2290.7,2498.3,1905.1,2085.2,1815.6,1730,1604.5,1420.2,957.8,1110.6,2193.5,2326.2,2511.5,1204.1,1538.2,1882.9,1346.6,2306.2,2422.5,1970.8,1799.4,1758.1,1628.2,1259.7,675.4,1075.6,1708.2,547.5,0,687.3],[1388.7,1750.6,1537.5,1388.7,2838.1,2477.4,2671.7,1959.2,1896.9,2517.9,2560.7,2523.2,2146.2,2239.9,2003.9,2211.5,1637.7,1823.7,1532.5,1632.9,1439.2,1254.9,947.9,945.3,1906.7,2019.1,2204.4,1352.3,1372.9,1575.8,1066.5,1999.1,2165.3,1663.7,1492.3,1451,1321.1,1094.4,1101.4,1501.6,1401.1,346.4,664.6,0]]

# Day 1 - Start at 8:00am at Location 1 (index 0)
# Day 1 - End at 4:00pm at Location 2 (index 1)
# Day 2 - Start at 6:00am at Location 3 (index 2)
# Day 2 - End at 6:00pm at Location 4 (index 3)
Windows = [[28800, 28800], [57600, 57600], [21600, 21600], [64800, 64800], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600], [24200, 59600]]

Durations = [0, 0, 0, 0, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 3600, 3600, 3600, 3600, 3600, 3600, 3600]

Penalties = [576460752303423487, 576460752303423487, 576460752303423487, 576460752303423487, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]

NUM_DAYS = 2

START_NODES = []
for node in range(0, NUM_DAYS):
  START_NODES.append(node * 2)

END_NODES = []
for node in range(0, NUM_DAYS):
  END_NODES.append(node * 2 + 1)

REGULAR_NODES = []
for node in range(NUM_DAYS * 2, len(Matrix)):
  REGULAR_NODES.append(node)

def transit_callback(from_index, to_index):

  # Returns the travel time plus service time between the two nodes.
  # Convert from routing variable Index to time matrix NodeIndex.
  from_node = manager.IndexToNode(from_index)
  to_node = manager.IndexToNode(to_index)

  return Matrix[from_node][to_node] + Durations[from_node]

# Create the routing index manager.
manager = pywrapcp.RoutingIndexManager(len(Matrix), 1, [0], [1])

# Create Routing Model.
routing = pywrapcp.RoutingModel(manager)

# Register the Transit Callback.
transit_callback_index = routing.RegisterTransitCallback(transit_callback)

# Set the arc cost evaluator for all vehicles
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Time Windows constraint.
routing.AddDimension(
  transit_callback_index,
  86400, # An upper bound for slack (the wait times at the locations).
  86400 * NUM_DAYS, # An upper bound for the total time over each vehicle's route.
  False, # Determine whether the cumulative variable is set to zero at the start of the vehicle's route.
  'Time')
time_dimension = routing.GetDimensionOrDie('Time')

# Allow all non-start and non-end nodes to be droppable.
for node in range(len(START_NODES) + len(END_NODES), len(Matrix)):
  routing.AddDisjunction([manager.NodeToIndex(node)], Penalties[node])

# Add time window constraints for all regular nodes.
for location_index, time_window in enumerate(Windows):
  if location_index in REGULAR_NODES:
    index = manager.NodeToIndex(location_index)

    # Add the range between the start of the first day and the end of the last day
    time_dimension.CumulVar(index).SetRange(0, 86400 * NUM_DAYS)

    for Day in range(NUM_DAYS):

      # Remove the range between the start of the day and the start of work
      time_dimension.CumulVar(index).RemoveInterval(Day * 86400, Windows[Day * 2][0] + (Day * 86400))

      # Remove the range between the start of the day and the start of location
      time_dimension.CumulVar(index).RemoveInterval(Day * 86400, time_window[0] + (Day * 86400))

      # Remove the range between the end of work and the end of the day
      time_dimension.CumulVar(index).RemoveInterval(Windows[(Day * 2) + 1][0] + (Day * 86400), 86400 + (Day * 86400))

      # Remove the range between the end of location and the end of the day
      time_dimension.CumulVar(index).RemoveInterval(time_window[1] + (Day * 86400), 86400 + (Day * 86400))


# Add time window constraints for start and end nodes.
# TODO: This also needs to be done for each additional day
index = routing.Start(0)
time_dimension.CumulVar(index).SetRange(Windows[0][0],Windows[0][1])
index = routing.End(0)
time_dimension.CumulVar(index).SetRange(
  Windows[1][0] + ((NUM_DAYS - 1) * 86400),
  Windows[1][1] + ((NUM_DAYS - 1) * 86400))

# Instantiate route start and end times to produce feasible times
routing.AddVariableMinimizedByFinalizer(time_dimension.CumulVar(routing.Start(0)))
routing.AddVariableMinimizedByFinalizer(time_dimension.CumulVar(routing.End(0)))

# Setting first solution heuristic. 
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Setting local search metaheuristics:
search_parameters.local_search_metaheuristic = (routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
search_parameters.time_limit.seconds = 5
search_parameters.log_search = False

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Print the results
print(f"Objective: {solution.ObjectiveValue()}")

# Return the dropped locations
dropped = []
for node in range(routing.Size()):
  if routing.IsStart(node) or routing.IsEnd(node):
    continue
  if solution.Value(routing.NextVar(node)) == node:
    dropped.append(manager.IndexToNode(node))
print(f"droped: {dropped}")

# Return the scheduled locations
index = routing.Start(0)
plan_output = 'Route for vehicle 0:\n'
while not routing.IsEnd(index):
  time = time_dimension.CumulVar(index)
  tw_min = solution.Min(time)
  if tw_min > 86400:
    tw_min = f"{tw_min%86400}+1day"
  tw_max = solution.Max(time)
  if tw_max > 86400:
    tw_max = f"{tw_max%86400}+1day"
  plan_output += f'{manager.IndexToNode(index)} [{tw_min};{tw_max}] -> '
  index = solution.Value(routing.NextVar(index))
time = time_dimension.CumulVar(index)
tw_min = solution.Min(time)
tw_max = solution.Max(time)
if tw_min > 86400:
  tw_min = f"{tw_min%86400}+1day"
tw_max = solution.Max(time)
if tw_max > 86400:
  tw_max = f"{tw_max%86400}+1day"
plan_output += f'{manager.IndexToNode(index)} [{tw_min};{tw_max}]'
print(plan_output)