%define major 6
%define libname %mklibname spatialindex
%define devname %mklibname spatialindex -d

Name: libspatialindex
Version: 1.9.3
Release: 1
Source0: https://github.com/libspatialindex/libspatialindex/archive/%{version}/%{name}-%{version}.tar.gz
Summary: Library for spatial indexing
URL: https://libspatialindex.org/
License: MIT
Group: System/Libraries
BuildRequires: cmake ninja

%description
The purpose of this library is to provide:
1. An extensible framework that will support robust spatial indexing methods.
2. Support for sophisticated spatial queries. Range, point location, nearest
   neighbor and k-nearest neighbor as well as parametric queries (defined by
  spatial constraints) should be easy to deploy and run.
3. Easy to use interfaces for inserting, deleting and updating information.
4. Wide variety of customization capabilities. Basic index and storage
   characteristics like the page size, node capacity, minimum fan-out,
   splitting algorithm, etc. should be easy to customize.
5. Index persistence. Internal memory and external memory structures should
   be supported. Clustered and non-clustered indices should be easy to be
   persisted.

%package -n %{libname}
Summary: Library for spatial indexing
Group: System/Libraries

%description -n %{libname}
The purpose of this library is to provide:
1. An extensible framework that will support robust spatial indexing methods.
2. Support for sophisticated spatial queries. Range, point location, nearest
   neighbor and k-nearest neighbor as well as parametric queries (defined by
  spatial constraints) should be easy to deploy and run.
3. Easy to use interfaces for inserting, deleting and updating information.
4. Wide variety of customization capabilities. Basic index and storage
   characteristics like the page size, node capacity, minimum fan-out,
   splitting algorithm, etc. should be easy to customize.
5. Index persistence. Internal memory and external memory structures should
   be supported. Clustered and non-clustered indices should be easy to be
   persisted.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

The purpose of this library is to provide:
1. An extensible framework that will support robust spatial indexing methods.
2. Support for sophisticated spatial queries. Range, point location, nearest
   neighbor and k-nearest neighbor as well as parametric queries (defined by
  spatial constraints) should be easy to deploy and run.
3. Easy to use interfaces for inserting, deleting and updating information.
4. Wide variety of customization capabilities. Basic index and storage
   characteristics like the page size, node capacity, minimum fan-out,
   splitting algorithm, etc. should be easy to customize.
5. Index persistence. Internal memory and external memory structures should
   be supported. Clustered and non-clustered indices should be easy to be
   persisted.

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
