# Файл config

## Расположение

```
~/.ssh/config
```

## Пример с ssh-ключём

```
Host <название>
  HostName <dns/ip>
  User <имя пользователя>
  IdentityFile ~/.ssh/<путь к закрытому ключу>
```

## Срисок параметров

| Директива | Описание |
|-----------|----------|
| **Host** | Имена/шаблоны, к которым применяются последующие параметры. |
| **HostName** | Фактическое имя/IP сервера. |
| **User** | Имя пользователя по умолчанию. |
| **Port** | Порт SSH‑демона. |
| **AddressFamily** | `any`, `inet`, `inet6`. |
| **BatchMode** | `yes` — отключает запрос пароля (полезно в скриптах). |
| **BindAddress** | Локальный IP, с которого будет исходить соединение. |
| **CanonicalDomains**, **CanonicalizeHostname**, **CanonicalizeMaxDots**, **CanonicalizeFallbackLocal** | Управление канонизацией имен. |
| **ChallengeResponseAuthentication** | Включить/отключить challenge‑response (обычно `no`). |
| **CheckHostIP** | Проверять IP‑адрес при проверке known_hosts. |
| **Ciphers**, **MACs**, **KexAlgorithms**, **HostKeyAlgorithms** | Списки криптографических алгоритмов. |
| **Compression**, **CompressionLevel** | Включить сжатие и задать уровень. |
| **ConnectionAttempts** | Кол‑во попыток соединения. |
| **ConnectTimeout** | Таймаут соединения в секундах. |
| **ControlMaster**, **ControlPath**, **ControlPersist** | Мультиплексирование соединений. |
| **DynamicForward** | SOCKS‑прокси (`DynamicForward 1080`). |
| **EscapeChar** | Символ экранирования (по‑умолчанию `~`). |
| **ExitOnForwardFailure** | Завершать клиент, если туннель не создался. |
| **FingerprintHash** | Хеш отпечатка (`md5`, `sha256`). |
| **ForwardAgent**, **ForwardX11**, **ForwardX11Trusted**, **ForwardX11Timeout** | Перенаправление агента, X11. |
| **GatewayPorts** | Разрешить прослушивание на всех интерфейсах для удалённых форвардов. |
| **GlobalKnownHostsFile** | Файл со списком известных хостов (глобальный). |
| **GSSAPIAuthentication**, **GSSAPIDelegateCredentials**, **GSSAPIKeyExchange**, **GSSAPITrustDNS** | Настройки GSSAPI/Kerberos. |
| **HostKeyAlgorithms** | Приоритет алгоритмов host‑key. |
| **IdentityFile**, **IdentityFile2**, **IdentityFile3** | Путь к приватным ключам (можно указать несколько). |
| **IdentitiesOnly** | Использовать только указанные в `IdentityFile`. |
| **IPQoS** | Установить QoS для трафика (например, `lowdelay`). |
| **KbdInteractiveAuthentication**, **PasswordAuthentication**, **PubkeyAuthentication**, **RhostsAuthentication**, **RSAAuthentication** | Способы аутентификации. |
| **KexAlgorithms** | Алгоритмы обмена ключами. |
| **LogLevel** | `QUIET`, `FATAL`, `ERROR`, `INFO`, `VERBOSE`, `DEBUG`, `DEBUG1…3`. |
| **MACs** | Список MAC‑алгоритмов. |
| **NoHostAuthenticationForLocalhost** | Отключать проверку known_hosts для localhost. |
| **NumberOfPasswordPrompts** | Сколько раз спрашивать пароль. |
| **PasswordAuthentication** | Включить/отключить парольную аутентификацию. |
| **PKCS11Provider** | Путь к PKCS#11‑модулю. |
| **Port** | Порт удалённого сервера. |
| **PreferredAuthentications** | Порядок методов аутентификации (`gssapi-with-mic,publickey,password`). |
| **Protocol** | Версия протокола (обычно `2`). |
| **ProxyCommand**, **ProxyJump**, **ProxyUseFdpass** | Прокси‑соединения. |
| **PubkeyAcceptedKeyTypes** | Приёмлемые типы публичных ключей. |
| **RekeyLimit** | Когда выполнять повторный обмен ключами. |
| **RemoteCommand** | Команда, которую выполнить сразу после входа. |
| **RemoteForward** | Перенаправление порта с сервера на клиент (`RemoteForward 9000 localhost:80`). |
| **RequestTTY** | `yes`, `no`, `force`, `auto`. |
| **SendEnv** | Переменные окружения, отправляемые на сервер. |
| **ServerAliveInterval**, **ServerAliveCountMax** | Пакеты keep‑alive от клиента к серверу. |
| **SetEnv** | Установить переменные окружения на клиенте. |
| **StrictHostKeyChecking** | `yes`, `no`, `ask`. |
| **TCPKeepAlive** | Использовать TCP keep‑alive. |
| **Tunnel**, **TunnelDevice** | Настройка VPN‑туннеля. |
| **UpdateHostKeys** | Обновлять known_hosts при изменении host‑key. |
| **User**, **UserKnownHostsFile** | Имя пользователя, файл known_hosts для конкретного хоста. |
| **VerifyHostKeyDNS** | Проверка хоста через DNS (SSHFP). |
| **VisualHostKey** | Показать ASCII‑графику отпечатка ключа. |
| **XAuthLocation** | Путь к `xauth`. |
| **Match** | Условный блок (по User, Group, Host, Address, LocalAddress). |