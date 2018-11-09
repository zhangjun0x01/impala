#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import Status.ttypes
import Types.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class StatestoreServiceVersion:
  V1 = 0

  _VALUES_TO_NAMES = {
    0: "V1",
  }

  _NAMES_TO_VALUES = {
    "V1": 0,
  }


class TPoolStats:
  """
  Attributes:
   - num_admitted_running
   - num_queued
   - backend_mem_reserved
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'num_admitted_running', None, None, ), # 1
    (2, TType.I64, 'num_queued', None, None, ), # 2
    (3, TType.I64, 'backend_mem_reserved', None, None, ), # 3
  )

  def __init__(self, num_admitted_running=None, num_queued=None, backend_mem_reserved=None,):
    self.num_admitted_running = num_admitted_running
    self.num_queued = num_queued
    self.backend_mem_reserved = backend_mem_reserved

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.num_admitted_running = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.num_queued = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.backend_mem_reserved = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TPoolStats')
    if self.num_admitted_running is not None:
      oprot.writeFieldBegin('num_admitted_running', TType.I64, 1)
      oprot.writeI64(self.num_admitted_running)
      oprot.writeFieldEnd()
    if self.num_queued is not None:
      oprot.writeFieldBegin('num_queued', TType.I64, 2)
      oprot.writeI64(self.num_queued)
      oprot.writeFieldEnd()
    if self.backend_mem_reserved is not None:
      oprot.writeFieldBegin('backend_mem_reserved', TType.I64, 3)
      oprot.writeI64(self.backend_mem_reserved)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.num_admitted_running is None:
      raise TProtocol.TProtocolException(message='Required field num_admitted_running is unset!')
    if self.num_queued is None:
      raise TProtocol.TProtocolException(message='Required field num_queued is unset!')
    if self.backend_mem_reserved is None:
      raise TProtocol.TProtocolException(message='Required field backend_mem_reserved is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TBackendDescriptor:
  """
  Attributes:
   - address
   - ip_address
   - is_coordinator
   - is_executor
   - debug_http_address
   - secure_webserver
   - krpc_address
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'address', (Types.ttypes.TNetworkAddress, Types.ttypes.TNetworkAddress.thrift_spec), None, ), # 1
    (2, TType.STRING, 'ip_address', None, None, ), # 2
    (3, TType.BOOL, 'is_coordinator', None, None, ), # 3
    (4, TType.BOOL, 'is_executor', None, None, ), # 4
    (5, TType.STRUCT, 'debug_http_address', (Types.ttypes.TNetworkAddress, Types.ttypes.TNetworkAddress.thrift_spec), None, ), # 5
    (6, TType.BOOL, 'secure_webserver', None, None, ), # 6
    (7, TType.STRUCT, 'krpc_address', (Types.ttypes.TNetworkAddress, Types.ttypes.TNetworkAddress.thrift_spec), None, ), # 7
  )

  def __init__(self, address=None, ip_address=None, is_coordinator=None, is_executor=None, debug_http_address=None, secure_webserver=None, krpc_address=None,):
    self.address = address
    self.ip_address = ip_address
    self.is_coordinator = is_coordinator
    self.is_executor = is_executor
    self.debug_http_address = debug_http_address
    self.secure_webserver = secure_webserver
    self.krpc_address = krpc_address

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.address = Types.ttypes.TNetworkAddress()
          self.address.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.ip_address = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.BOOL:
          self.is_coordinator = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.BOOL:
          self.is_executor = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRUCT:
          self.debug_http_address = Types.ttypes.TNetworkAddress()
          self.debug_http_address.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.BOOL:
          self.secure_webserver = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRUCT:
          self.krpc_address = Types.ttypes.TNetworkAddress()
          self.krpc_address.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TBackendDescriptor')
    if self.address is not None:
      oprot.writeFieldBegin('address', TType.STRUCT, 1)
      self.address.write(oprot)
      oprot.writeFieldEnd()
    if self.ip_address is not None:
      oprot.writeFieldBegin('ip_address', TType.STRING, 2)
      oprot.writeString(self.ip_address)
      oprot.writeFieldEnd()
    if self.is_coordinator is not None:
      oprot.writeFieldBegin('is_coordinator', TType.BOOL, 3)
      oprot.writeBool(self.is_coordinator)
      oprot.writeFieldEnd()
    if self.is_executor is not None:
      oprot.writeFieldBegin('is_executor', TType.BOOL, 4)
      oprot.writeBool(self.is_executor)
      oprot.writeFieldEnd()
    if self.debug_http_address is not None:
      oprot.writeFieldBegin('debug_http_address', TType.STRUCT, 5)
      self.debug_http_address.write(oprot)
      oprot.writeFieldEnd()
    if self.secure_webserver is not None:
      oprot.writeFieldBegin('secure_webserver', TType.BOOL, 6)
      oprot.writeBool(self.secure_webserver)
      oprot.writeFieldEnd()
    if self.krpc_address is not None:
      oprot.writeFieldBegin('krpc_address', TType.STRUCT, 7)
      self.krpc_address.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.address is None:
      raise TProtocol.TProtocolException(message='Required field address is unset!')
    if self.ip_address is None:
      raise TProtocol.TProtocolException(message='Required field ip_address is unset!')
    if self.is_coordinator is None:
      raise TProtocol.TProtocolException(message='Required field is_coordinator is unset!')
    if self.is_executor is None:
      raise TProtocol.TProtocolException(message='Required field is_executor is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TTopicItem:
  """
  Attributes:
   - key
   - value
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'key', None, None, ), # 1
    (2, TType.STRING, 'value', None, None, ), # 2
  )

  def __init__(self, key=None, value=None,):
    self.key = key
    self.value = value

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.key = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.value = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TTopicItem')
    if self.key is not None:
      oprot.writeFieldBegin('key', TType.STRING, 1)
      oprot.writeString(self.key)
      oprot.writeFieldEnd()
    if self.value is not None:
      oprot.writeFieldBegin('value', TType.STRING, 2)
      oprot.writeString(self.value)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.key is None:
      raise TProtocol.TProtocolException(message='Required field key is unset!')
    if self.value is None:
      raise TProtocol.TProtocolException(message='Required field value is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TTopicDelta:
  """
  Attributes:
   - topic_name
   - topic_entries
   - topic_deletions
   - is_delta
   - from_version
   - to_version
   - min_subscriber_topic_version
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'topic_name', None, None, ), # 1
    (2, TType.LIST, 'topic_entries', (TType.STRUCT,(TTopicItem, TTopicItem.thrift_spec)), None, ), # 2
    (3, TType.LIST, 'topic_deletions', (TType.STRING,None), None, ), # 3
    (4, TType.BOOL, 'is_delta', None, None, ), # 4
    (5, TType.I64, 'from_version', None, None, ), # 5
    (6, TType.I64, 'to_version', None, None, ), # 6
    (7, TType.I64, 'min_subscriber_topic_version', None, None, ), # 7
  )

  def __init__(self, topic_name=None, topic_entries=None, topic_deletions=None, is_delta=None, from_version=None, to_version=None, min_subscriber_topic_version=None,):
    self.topic_name = topic_name
    self.topic_entries = topic_entries
    self.topic_deletions = topic_deletions
    self.is_delta = is_delta
    self.from_version = from_version
    self.to_version = to_version
    self.min_subscriber_topic_version = min_subscriber_topic_version

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.topic_name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.topic_entries = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = TTopicItem()
            _elem5.read(iprot)
            self.topic_entries.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.topic_deletions = []
          (_etype9, _size6) = iprot.readListBegin()
          for _i10 in xrange(_size6):
            _elem11 = iprot.readString();
            self.topic_deletions.append(_elem11)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.BOOL:
          self.is_delta = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I64:
          self.from_version = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I64:
          self.to_version = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I64:
          self.min_subscriber_topic_version = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TTopicDelta')
    if self.topic_name is not None:
      oprot.writeFieldBegin('topic_name', TType.STRING, 1)
      oprot.writeString(self.topic_name)
      oprot.writeFieldEnd()
    if self.topic_entries is not None:
      oprot.writeFieldBegin('topic_entries', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.topic_entries))
      for iter12 in self.topic_entries:
        iter12.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.topic_deletions is not None:
      oprot.writeFieldBegin('topic_deletions', TType.LIST, 3)
      oprot.writeListBegin(TType.STRING, len(self.topic_deletions))
      for iter13 in self.topic_deletions:
        oprot.writeString(iter13)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.is_delta is not None:
      oprot.writeFieldBegin('is_delta', TType.BOOL, 4)
      oprot.writeBool(self.is_delta)
      oprot.writeFieldEnd()
    if self.from_version is not None:
      oprot.writeFieldBegin('from_version', TType.I64, 5)
      oprot.writeI64(self.from_version)
      oprot.writeFieldEnd()
    if self.to_version is not None:
      oprot.writeFieldBegin('to_version', TType.I64, 6)
      oprot.writeI64(self.to_version)
      oprot.writeFieldEnd()
    if self.min_subscriber_topic_version is not None:
      oprot.writeFieldBegin('min_subscriber_topic_version', TType.I64, 7)
      oprot.writeI64(self.min_subscriber_topic_version)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.topic_name is None:
      raise TProtocol.TProtocolException(message='Required field topic_name is unset!')
    if self.topic_entries is None:
      raise TProtocol.TProtocolException(message='Required field topic_entries is unset!')
    if self.topic_deletions is None:
      raise TProtocol.TProtocolException(message='Required field topic_deletions is unset!')
    if self.is_delta is None:
      raise TProtocol.TProtocolException(message='Required field is_delta is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TTopicRegistration:
  """
  Attributes:
   - topic_name
   - is_transient
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'topic_name', None, None, ), # 1
    (2, TType.BOOL, 'is_transient', None, None, ), # 2
  )

  def __init__(self, topic_name=None, is_transient=None,):
    self.topic_name = topic_name
    self.is_transient = is_transient

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.topic_name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BOOL:
          self.is_transient = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TTopicRegistration')
    if self.topic_name is not None:
      oprot.writeFieldBegin('topic_name', TType.STRING, 1)
      oprot.writeString(self.topic_name)
      oprot.writeFieldEnd()
    if self.is_transient is not None:
      oprot.writeFieldBegin('is_transient', TType.BOOL, 2)
      oprot.writeBool(self.is_transient)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.topic_name is None:
      raise TProtocol.TProtocolException(message='Required field topic_name is unset!')
    if self.is_transient is None:
      raise TProtocol.TProtocolException(message='Required field is_transient is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TRegisterSubscriberRequest:
  """
  Attributes:
   - protocol_version
   - subscriber_id
   - subscriber_location
   - topic_registrations
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'protocol_version', None,     0, ), # 1
    (2, TType.STRING, 'subscriber_id', None, None, ), # 2
    (3, TType.STRUCT, 'subscriber_location', (Types.ttypes.TNetworkAddress, Types.ttypes.TNetworkAddress.thrift_spec), None, ), # 3
    (4, TType.LIST, 'topic_registrations', (TType.STRUCT,(TTopicRegistration, TTopicRegistration.thrift_spec)), None, ), # 4
  )

  def __init__(self, protocol_version=thrift_spec[1][4], subscriber_id=None, subscriber_location=None, topic_registrations=None,):
    self.protocol_version = protocol_version
    self.subscriber_id = subscriber_id
    self.subscriber_location = subscriber_location
    self.topic_registrations = topic_registrations

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.protocol_version = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.subscriber_id = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.subscriber_location = Types.ttypes.TNetworkAddress()
          self.subscriber_location.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.topic_registrations = []
          (_etype17, _size14) = iprot.readListBegin()
          for _i18 in xrange(_size14):
            _elem19 = TTopicRegistration()
            _elem19.read(iprot)
            self.topic_registrations.append(_elem19)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TRegisterSubscriberRequest')
    if self.protocol_version is not None:
      oprot.writeFieldBegin('protocol_version', TType.I32, 1)
      oprot.writeI32(self.protocol_version)
      oprot.writeFieldEnd()
    if self.subscriber_id is not None:
      oprot.writeFieldBegin('subscriber_id', TType.STRING, 2)
      oprot.writeString(self.subscriber_id)
      oprot.writeFieldEnd()
    if self.subscriber_location is not None:
      oprot.writeFieldBegin('subscriber_location', TType.STRUCT, 3)
      self.subscriber_location.write(oprot)
      oprot.writeFieldEnd()
    if self.topic_registrations is not None:
      oprot.writeFieldBegin('topic_registrations', TType.LIST, 4)
      oprot.writeListBegin(TType.STRUCT, len(self.topic_registrations))
      for iter20 in self.topic_registrations:
        iter20.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.protocol_version is None:
      raise TProtocol.TProtocolException(message='Required field protocol_version is unset!')
    if self.subscriber_id is None:
      raise TProtocol.TProtocolException(message='Required field subscriber_id is unset!')
    if self.subscriber_location is None:
      raise TProtocol.TProtocolException(message='Required field subscriber_location is unset!')
    if self.topic_registrations is None:
      raise TProtocol.TProtocolException(message='Required field topic_registrations is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TRegisterSubscriberResponse:
  """
  Attributes:
   - status
   - registration_id
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'status', (Status.ttypes.TStatus, Status.ttypes.TStatus.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'registration_id', (Types.ttypes.TUniqueId, Types.ttypes.TUniqueId.thrift_spec), None, ), # 2
  )

  def __init__(self, status=None, registration_id=None,):
    self.status = status
    self.registration_id = registration_id

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.status = Status.ttypes.TStatus()
          self.status.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.registration_id = Types.ttypes.TUniqueId()
          self.registration_id.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TRegisterSubscriberResponse')
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.STRUCT, 1)
      self.status.write(oprot)
      oprot.writeFieldEnd()
    if self.registration_id is not None:
      oprot.writeFieldBegin('registration_id', TType.STRUCT, 2)
      self.registration_id.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.status is None:
      raise TProtocol.TProtocolException(message='Required field status is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TUpdateStateRequest:
  """
  Attributes:
   - protocol_version
   - topic_deltas
   - registration_id
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'protocol_version', None,     0, ), # 1
    (2, TType.MAP, 'topic_deltas', (TType.STRING,None,TType.STRUCT,(TTopicDelta, TTopicDelta.thrift_spec)), None, ), # 2
    (3, TType.STRUCT, 'registration_id', (Types.ttypes.TUniqueId, Types.ttypes.TUniqueId.thrift_spec), None, ), # 3
  )

  def __init__(self, protocol_version=thrift_spec[1][4], topic_deltas=None, registration_id=None,):
    self.protocol_version = protocol_version
    self.topic_deltas = topic_deltas
    self.registration_id = registration_id

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.protocol_version = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.MAP:
          self.topic_deltas = {}
          (_ktype22, _vtype23, _size21 ) = iprot.readMapBegin() 
          for _i25 in xrange(_size21):
            _key26 = iprot.readString();
            _val27 = TTopicDelta()
            _val27.read(iprot)
            self.topic_deltas[_key26] = _val27
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.registration_id = Types.ttypes.TUniqueId()
          self.registration_id.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TUpdateStateRequest')
    if self.protocol_version is not None:
      oprot.writeFieldBegin('protocol_version', TType.I32, 1)
      oprot.writeI32(self.protocol_version)
      oprot.writeFieldEnd()
    if self.topic_deltas is not None:
      oprot.writeFieldBegin('topic_deltas', TType.MAP, 2)
      oprot.writeMapBegin(TType.STRING, TType.STRUCT, len(self.topic_deltas))
      for kiter28,viter29 in self.topic_deltas.items():
        oprot.writeString(kiter28)
        viter29.write(oprot)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.registration_id is not None:
      oprot.writeFieldBegin('registration_id', TType.STRUCT, 3)
      self.registration_id.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.protocol_version is None:
      raise TProtocol.TProtocolException(message='Required field protocol_version is unset!')
    if self.topic_deltas is None:
      raise TProtocol.TProtocolException(message='Required field topic_deltas is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TUpdateStateResponse:
  """
  Attributes:
   - status
   - topic_updates
   - skipped
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'status', (Status.ttypes.TStatus, Status.ttypes.TStatus.thrift_spec), None, ), # 1
    (2, TType.LIST, 'topic_updates', (TType.STRUCT,(TTopicDelta, TTopicDelta.thrift_spec)), None, ), # 2
    (3, TType.BOOL, 'skipped', None, None, ), # 3
  )

  def __init__(self, status=None, topic_updates=None, skipped=None,):
    self.status = status
    self.topic_updates = topic_updates
    self.skipped = skipped

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.status = Status.ttypes.TStatus()
          self.status.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.topic_updates = []
          (_etype33, _size30) = iprot.readListBegin()
          for _i34 in xrange(_size30):
            _elem35 = TTopicDelta()
            _elem35.read(iprot)
            self.topic_updates.append(_elem35)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.BOOL:
          self.skipped = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TUpdateStateResponse')
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.STRUCT, 1)
      self.status.write(oprot)
      oprot.writeFieldEnd()
    if self.topic_updates is not None:
      oprot.writeFieldBegin('topic_updates', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.topic_updates))
      for iter36 in self.topic_updates:
        iter36.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.skipped is not None:
      oprot.writeFieldBegin('skipped', TType.BOOL, 3)
      oprot.writeBool(self.skipped)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.status is None:
      raise TProtocol.TProtocolException(message='Required field status is unset!')
    if self.topic_updates is None:
      raise TProtocol.TProtocolException(message='Required field topic_updates is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class THeartbeatRequest:
  """
  Attributes:
   - registration_id
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'registration_id', (Types.ttypes.TUniqueId, Types.ttypes.TUniqueId.thrift_spec), None, ), # 1
  )

  def __init__(self, registration_id=None,):
    self.registration_id = registration_id

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.registration_id = Types.ttypes.TUniqueId()
          self.registration_id.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('THeartbeatRequest')
    if self.registration_id is not None:
      oprot.writeFieldBegin('registration_id', TType.STRUCT, 1)
      self.registration_id.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class THeartbeatResponse:

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('THeartbeatResponse')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)