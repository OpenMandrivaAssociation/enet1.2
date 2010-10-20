%define major 0
%define libname %mklibname enet %{major}
%define develname %mklibname enet -d

Name:		libenet
Version:	1.2.2
Release:	%mkrel 1
Summary:	Simple Network Communication Layer on Top of UDP
License:	BSD
Group:		System/Libraries
Url:		http://enet.bespin.org/
Source:		enet-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
ENet's purpose is to provide a relatively thin, simple and robust network 
communication layer on top of UDP (User Datagram Protocol). The primary 
feature it provides is optional reliable, in-order delivery of packets.

ENet omits certain higher level networking features such as authentication, 
lobbying, server discovery, encryption, or other similar tasks that are 
particularly application specific so that the library remains flexible, 
portable, and easily embeddable.

%package -n	%{libname}
Group:		System/Libraries
Summary:	Simple Network Communication Layer on Top of UDP

%description -n %{libname}
ENet's purpose is to provide a relatively thin, simple and robust network 
communication layer on top of UDP (User Datagram Protocol). The primary 
feature it provides is optional reliable, in-order delivery of packets.

ENet omits certain higher level networking features such as authentication, 
lobbying, server discovery, encryption, or other similar tasks that are 
particularly application specific so that the library remains flexible, 
portable, and easily embeddable.

%package -n	%{develname}
Group:		Development/C
Provides:   %{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Summary:	Simple Network Communication Layer on Top of UDP

%description -n	%{develname}
ENet's purpose is to provide a relatively thin, simple and robust network
communication layer on top of UDP (User Datagram Protocol). The primary
feature it provides is optional reliable, in-order delivery of packets.

ENet omits certain higher level networking features such as authentication,
lobbying, server discovery, encryption, or other similar tasks that are
particularly application specific so that the library remains flexible,
portable, and easily embeddable.


%prep
%setup -qn enet-%{version}

%build
%configure2_5x --disable-static
%make

%install
%makeinstall

%check
%make check

%clean
rm -rf "%{buildroot}"

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libenet.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/enet
%{_libdir}/libenet.so
%{_libdir}/libenet.la
%{_libdir}/pkgconfig/libenet.pc

