class TaskDispatch(Base,Table):
	__tablename__ = 'or_task_dispatch'
	msg_id = Column(String,primary_key=False,nullable=False)
	msg_create_date = Column(DateTime,primary_key=False,nullable=True)
	msg_deal_date = Column(DateTime,primary_key=False,nullable=True)
	msg_deal_flag = Column(CHAR(1),primary_key=False,nullable=True)
	msg_deal_count = Column(BIGINT(2),primary_key=False,nullable=True)
	msg_fail_reason = Column(String,primary_key=False,nullable=True)
	so_nbr = Column(String,primary_key=False,nullable=True)
	remarks = Column(String,primary_key=False,nullable=True)
	province_code = Column(String,primary_key=False,nullable=True)
	partition_id = Column(BIGINT(20),primary_key=False,nullable=True)
	task_type = Column(String,primary_key=False,nullable=True)
	wf_id = Column(String,primary_key=False,nullable=True)
