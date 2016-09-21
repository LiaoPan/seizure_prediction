# -*- coding: utf-8 -*-

class DataSet:
	def __init__(self, no_channels, no_seizure_files, no_normal_files, no_seizure, no_normal, base_name, set_name, user, blacklisted_samples=None):
		self.no_channels = no_channels
		self.no_seizure_files = no_seizure_files
		self.no_normal_files = no_normal_files
		self.no_seizure = no_seizure
		self.no_normal = no_normal
		self.base_name = base_name
		self.set_name = set_name
		self.blacklisted_samples = blacklisted_samples
		if self.blacklisted_samples == None:
			self.blacklisted_samples = []
		self.enabled = True
		self.debug_sub_ratio = 1
	def __str__(self):
		return "name: %s, type: %s, user: %s, hand: %s, files: %d"%(self.session_name, self.type, self.user, self.hand, self.noSamples())
	def noSamples(self):
		return len(self.fileIndices())
	def fileIndices(self):
		if not self.enabled:
			return []
		all_indices = xrange(int(self.no_files * self.debug_sub_ratio))
		filtered_indices = filter(lambda i: i not in self.blacklisted_samples, all_indices)
		return filtered_indices
	def fileName(self, index, channel):
		return '%s/%s%d_ch%d.raw'%(self.session_name, self.base_name, index, channel)
	__repr__ = __str__


patient0 = DataSet(no_channels=16,
                    no_seizure_files = 150,
                    no_normal_files = 1152,
                    no_seizure = 25,
                    no_normal = 192,
                    base_name="1_",
                    set_name="train_1",
                    user="patient0")

patient1 = DataSet(no_channels=16,
                    no_seizure_files = 150,
                    no_normal_files = 2196,
                    no_seizure = 25,
                    no_normal = 366,
                    base_name="2_",
                    set_name="train_2",
                    user="patient1")

patient2 = DataSet(no_channels=16,
                    no_seizure_files = 150,
                    no_normal_files = 1152,
                    no_seizure = 25,
                    no_normal = 192,
                    base_name="3_",
                    set_name="train_3",
                    user="patient2")

#TDOD add a noise session

all = [patient0, patient1, patient2]