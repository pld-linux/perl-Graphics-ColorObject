#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Graphics
%define		pnam	ColorObject
Summary:	Convert between color spaces
Summary(pl.UTF-8):	Przekształcenia między przestrzeniami kolorów
Name:		perl-Graphics-ColorObject
Version:	0.5.0
Release:	1
# same as perl
License:	GPL v1+ or Artistic	
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Graphics/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3b806cf21c97d9804bf2c0a300f48a0d
URL:		http://search.cpan.org/dist/Graphics-ColorObject/
BuildRequires:	perl-Graphics-ColorNames
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert between color spaces.

%description -l pl.UTF-8
Przekształcenia między przestrzeniami kolorów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Graphics/ColorObject.pm
%{_mandir}/man3/*
