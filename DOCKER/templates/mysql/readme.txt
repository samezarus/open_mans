Settings:

    All settings are stored in a file ".env":

        # global
        TZ - time zone

        # db
        DB                  - container name
        DB_PORT             - internal port for db
        DB_PORT_EXT         - external db(container port) (DB_PORT_EXT -> DB_PORT)
        DB_NAME             - db name
        DB_USER             - db user name
        DB_PASSWORD         - password for DB_USER
        DB_ROOT             - root user
        DB_PASSWORD_ROOT    - password for DB_ROOT
        DB_BACKUP_FOLDER    - root folder for backups
        DB_BACKUP_PREFIX    - prifix for backup file

    It is also important to re-interpret "docker-compose.yml -> services -> mysql-test" in DB

Usage:

    Copy "https://github.com/samezarus/open_mans/tree/ee159db0949ab0455fe694c93111378a476ae382/DOCKER/templates/mysql" to your folder.

    Up container:

        make up
    
    Down container:

        make down

    Hard restart:

        make restart_h
    
    Connect to CLI:

        make console
    
    View log's:

        make logs
    
    Without compression:
    
        Create dump:

            make backup ( $(DB_BACKUP_FOLDER)/$(DB_BACKUP_PREFIX).sql )

        Create dump+timestamp:

            make backup_ts ( $(DB_BACKUP_FOLDER)/$(DB_BACKUP_PREFIX)_<timestamp>.sql )

        Restore ( Without backup current db )

            make restore_h

        Restore ( With backup current db )

            make restore_s ( Before restore is called "make backup_ts" )
    
    With compression:

        Create dump:

            make backup_arc ( $(DB_BACKUP_FOLDER)/$(DB_BACKUP_PREFIX).gz )

        Create dump+timestamp:

            make backup_arc_ts ( $(DB_BACKUP_FOLDER)/$(DB_BACKUP_PREFIX)_<timestamp>.gz )

        Restore ( Without backup current db )

            make restore_arc_h

        Restore ( With backup current db )

            make restore_arc_s ( Before restore is called "make backup_arc_ts" )
