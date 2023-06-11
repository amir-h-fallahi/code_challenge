<?php

$username = isset($_GET["username"]) ? trim($_GET["username"]) : "user";

$safe_html = htmlspecialchars($username);

$output = Normalizer::normalize($safe_html, Normalizer::FORM_KC);

echo "Welcome " . $output;

?>
