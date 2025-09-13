SELECT
  CONCAT('/home/grep/src/', b.board_id, '/', f.file_id, f.file_name, f.file_ext)
  AS file_path
FROM used_goods_board b
JOIN used_goods_file  f ON f.board_id = b.board_id
WHERE b.views = (SELECT MAX(views) FROM used_goods_board)
ORDER BY f.file_id DESC;