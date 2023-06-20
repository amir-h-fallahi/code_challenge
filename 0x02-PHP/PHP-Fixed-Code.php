<?php

$username = isset($_GET["username"]) ? trim($_GET["username"]) : "user";

$output = Normalizer::normalize($username, Normalizer::FORM_KC);

$safe_html = htmlspecialchars($output);

echo "Welcome " . $safe_html;

?>
