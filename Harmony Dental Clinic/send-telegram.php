<?php
// ======================================
// Harmony Clinic — Telegram Lead Bot
// ======================================
// НАСТРОЙКА: вставьте свои данные ниже
// ======================================

$botToken   = 'YOUR_BOT_TOKEN';   // токен от @BotFather
$chatId     = 'YOUR_CHAT_ID';     // ID чата/группы

// ======================================

header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: https://harmonyclinic.od.ua');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['ok' => false, 'error' => 'Method not allowed']);
    exit;
}

$input = json_decode(file_get_contents('php://input'), true);

$name  = trim($input['name']  ?? '');
$phone = trim($input['phone'] ?? '');
$page  = trim($input['page']  ?? 'Головна');

if ($name === '' || $phone === '') {
    http_response_code(400);
    echo json_encode(['ok' => false, 'error' => 'Name and phone required']);
    exit;
}

$date = date('d.m.Y H:i');

$text  = "🦷 <b>Нова заявка з сайту!</b>\n";
$text .= "━━━━━━━━━━━━━━━━\n";
$text .= "👤 Ім'я: <b>" . htmlspecialchars($name) . "</b>\n";
$text .= "📱 Телефон: " . htmlspecialchars($phone) . "\n";
$text .= "📄 Сторінка: " . htmlspecialchars($page) . "\n";
$text .= "🕐 Час: " . $date . "\n";
$text .= "━━━━━━━━━━━━━━━━";

$url = "https://api.telegram.org/bot{$botToken}/sendMessage";
$payload = [
    'chat_id'    => $chatId,
    'text'       => $text,
    'parse_mode' => 'HTML',
];

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_TIMEOUT, 10);
$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

$result = json_decode($response, true);

if ($httpCode === 200 && ($result['ok'] ?? false)) {
    echo json_encode(['ok' => true]);
} else {
    http_response_code(502);
    echo json_encode(['ok' => false, 'error' => 'Telegram API error']);
}
