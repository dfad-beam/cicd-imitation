  <?php
// Сдвиг категории вверх/вниз

$id = (int)(trim($_REQUEST['id']));
$up = (int)(trim($_REQUEST['up']));


// Вначале определим, кого двигаем
$id1 = (int)(SQLCount("SELECT id FROM categories WHERE id='$id'"));
if ($id1 > 0) // (Такая подстраховка)
{
  $pos1 = (int)(SQLCount("SELECT pos FROM categories WHERE id='$id1'"));
  $pos2 = $pos1;
  ($up ? $pos2-- : $pos2++);
  $id2 = (int)(SQLCount("SELECT id FROM categories WHERE pos='$pos2'"));
  //print "-=$id1: $pos1 &lt;=&gt; $id2: $pos2=-<br>\n";

  if ($id2 > 0)
  {
    $req = "LOCK TABLES `categories` WRITE;";
    $result = mysql_query($req) or die("Ошибка БД: " . mysql_error());

    $req = "UPDATE categories SET pos='$pos2' WHERE id='$id1';";
    $result = mysql_query($req) or die("Ошибка БД: " . mysql_error());
    $req = "UPDATE categories SET pos='$pos1' WHERE id='$id2';";
    $result = mysql_query($req) or die("Ошибка БД: " . mysql_error());

    $req = "UNLOCK TABLES;";
    $result = mysql_query($req) or die("Ошибка БД: " . mysql_error());
  }
}
header("Location: ?action=categs");

?>