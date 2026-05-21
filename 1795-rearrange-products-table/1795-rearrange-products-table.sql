# Write your MySQL query statement below
SELECT 
    p.product_id,
    t.store,
    # 根據虛擬小表的店名，精準把大表裡那一欄的價格拿出來
    CASE 
        WHEN t.store = 'store1' THEN p.store1
        WHEN t.store = 'store2' THEN p.store2
        WHEN t.store = 'store3' THEN p.store3
    END AS price
FROM products p
# 這裡用 CROSS JOIN 串接一個用 UNION 憑空做出來的 3 列小表
CROSS JOIN (
    SELECT 'store1' AS store UNION ALL
    SELECT 'store2' AS store UNION ALL
    SELECT 'store3' AS store
) t
# 關鍵過濾：最後只留下「拿出來的價格不是 NULL」的資料
WHERE 
    CASE 
        WHEN t.store = 'store1' THEN p.store1
        WHEN t.store = 'store2' THEN p.store2
        WHEN t.store = 'store3' THEN p.store3
    END IS NOT NULL;

/*
# 1. 先撈 store1 的資料，並自己手動補上一個叫 'store1' 的字串標籤
SELECT product_id, 'store1' AS store, store1 AS price
FROM products
WHERE store1 IS NOT NULL  # 題目規定：如果價格是 NULL 就不要顯示

UNION ALL

# 2. 垂直拼貼 store2 的資料
SELECT product_id, 'store2' AS store, store2 AS price
FROM products
WHERE store2 IS NOT NULL

UNION ALL

# 3. 垂直拼貼 store3 的資料
SELECT product_id, 'store3' AS store, store3 AS price
FROM products
WHERE store3 IS NOT NULL;
*/