%define major 0
%define libname %mklibname enet 1.2 %{major}
%define develname %mklibname enet 1.2 -d

Name:		enet1.2
Version:	1.2.4
Release:	%mkrel 1
Summary:	Simple Network Communication Layer on Top of UDP
License:	BSD
Group:		System/Libraries
Url:		http://enet.bespin.org/
Source:		http://enet.bespin.org/download/enet-%{version}.tar.gz

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
Provides:	%{name}-devel = %{version}-%{release}
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
%makeinstall_std

#we don't want these
rm -rf %{buildroot}%{_libdir}/libenet.la

%check
%make check

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libenet.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/enet
%{_libdir}/libenet.so
%{_libdir}/pkgconfig/libenet.pc
