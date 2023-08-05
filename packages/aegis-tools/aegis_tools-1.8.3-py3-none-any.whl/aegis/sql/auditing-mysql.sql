CREATE TABLE audit_request_data (
  audit_request_data_id BIGINT NOT NULL AUTO_INCREMENT,
  audit_request_id BIGINT NOT NULL REFERENCES audit_request(audit_request_id),
  audit_session_id BIGINT NOT NULL REFERENCES audit_session(audit_session_id),
  request_url TEXT NOT NULL,
  request_method TEXT NOT NULL,
  request_bytes BIGINT NOT NULL,
  run_host VARCHAR(50) DEFAULT NULL,
  run_env VARCHAR(50) DEFAULT NULL,
  response_bytes BIGINT DEFAULT NULL,
  response_ms BIGINT DEFAULT NULL,
  response_status INTEGER DEFAULT NULL,
  request_headers TEXT NOT NULL,
  request_body MEDIUMTEXT NOT NULL,
  response_headers TEXT DEFAULT NULL,
  response_body MEDIUMTEXT DEFAULT NULL,
  response_error TEXT DEFAULT NULL,
  create_dttm timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  update_dttm timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  delete_dttm datetime DEFAULT NULL,
  PRIMARY KEY (audit_request_data_id),
  KEY audit_session_id (audit_session_id),
  KEY audit_request_id (audit_request_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
