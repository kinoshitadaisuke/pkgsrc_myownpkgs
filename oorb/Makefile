# $NetBSD$

DISTNAME=	oorb-1.3.0
CATEGORIES=	math
MASTER_SITES=	${MASTER_SITE_GITHUB:=oorb/}
GITHUB_PROJECT=	oorb
GITHUB_TAG=	refs/tags/v${PKGVERSION_NOREV}

DISTFILES+=	${DISTNAME}${EXTRACT_SUFX}
DISTFILES+=	header.430_229
SITES.header.430_229=	ftp://ssd.jpl.nasa.gov/pub/eph/planets/ascii/de430/
DISTFILES+=	ascp1550.430
SITES.ascp1550.430=	ftp://ssd.jpl.nasa.gov/pub/eph/planets/ascii/de430/
DISTFILES+=	ascp1650.430
SITES.ascp1650.430=	ftp://ssd.jpl.nasa.gov/pub/eph/planets/ascii/de430/
DISTFILES+=	ascp1750.430
SITES.ascp1750.430=	ftp://ssd.jpl.nasa.gov/pub/eph/planets/ascii/de430/
DISTFILES+=	ascp1850.430
SITES.ascp1850.430=	ftp://ssd.jpl.nasa.gov/pub/eph/planets/ascii/de430/
DISTFILES+=	ascp1950.430
SITES.ascp1950.430=	ftp://ssd.jpl.nasa.gov/pub/eph/planets/ascii/de430/
DISTFILES+=	ascp2050.430
SITES.ascp2050.430=	ftp://ssd.jpl.nasa.gov/pub/eph/planets/ascii/de430/
DISTFILES+=	ascp2150.430
SITES.ascp2150.430=	ftp://ssd.jpl.nasa.gov/pub/eph/planets/ascii/de430/
DISTFILES+=	ascp2250.430
SITES.ascp2250.430=	ftp://ssd.jpl.nasa.gov/pub/eph/planets/ascii/de430/
DISTFILES+=	ascp2350.430
SITES.ascp2350.430=	ftp://ssd.jpl.nasa.gov/pub/eph/planets/ascii/de430/
DISTFILES+=	ascp2450.430
SITES.ascp2450.430=	ftp://ssd.jpl.nasa.gov/pub/eph/planets/ascii/de430/
DISTFILES+=	ascp2550.430
SITES.ascp2550.430=	ftp://ssd.jpl.nasa.gov/pub/eph/planets/ascii/de430/
DISTFILES+=	testpo.430
SITES.testpo.430=	ftp://ssd.jpl.nasa.gov/pub/eph/planets/ascii/de430/

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/oorb/oorb/
COMMENT=	Open-source orbit-computation package for Solar System objects
LICENSE=	gpl-3.0

WRKSRC=	${WRKDIR}/${DISTNAME}

USE_LANGUAGES+=	fortran

DEPENDS+=	bash>=0:../../shells/bash
DEPENDS+=	curl>=0:../../www/curl
DEPENDS+=	gcc12>=0:../../lang/gcc12
DEPENDS+=	ghostscript-agpl>=0:../../print/ghostscript-agpl
DEPENDS+=	gmake>=0:../../devel/gmake
DEPENDS+=	gnuplot>=0:../../graphics/gnuplot
DEPENDS+=	dvipsk>=0:../../print/dvipsk
DEPENDS+=	tex-ae>=0:../../fonts/tex-ae
DEPENDS+=	tex-acronym>=0:../../print/tex-acronym
DEPENDS+=	tex-bigfoot>=0:../../print/tex-bigfoot
DEPENDS+=	wget>=0:../../net/wget

do-configure:
	(cd ${WRKSRC}; \
	bash ./configure gfortran opt;)

pre-build:
	(cd ${WRKSRC}/doc; \
	latex OpenOrb_Tutorial.tex; \
	latex OpenOrb_Tutorial.tex; \
	dvips OpenOrb_Tutorial.dvi; \
	ps2pdfwr OpenOrb_Tutorial.ps;)
	(cd ${WRKSRC}/data/JPL_ephemeris; \
        ${CP} -pf ${PKGSRCDIR}/distfiles/header.430_229 .; \
        ${CP} -pf ${PKGSRCDIR}/distfiles/ascp1550.430 .; \
        ${CP} -pf ${PKGSRCDIR}/distfiles/ascp1650.430 .; \
        ${CP} -pf ${PKGSRCDIR}/distfiles/ascp1750.430 .; \
        ${CP} -pf ${PKGSRCDIR}/distfiles/ascp1850.430 .; \
        ${CP} -pf ${PKGSRCDIR}/distfiles/ascp1950.430 .; \
        ${CP} -pf ${PKGSRCDIR}/distfiles/ascp2050.430 .; \
        ${CP} -pf ${PKGSRCDIR}/distfiles/ascp2150.430 .; \
        ${CP} -pf ${PKGSRCDIR}/distfiles/ascp2250.430 .; \
        ${CP} -pf ${PKGSRCDIR}/distfiles/ascp2350.430 .; \
        ${CP} -pf ${PKGSRCDIR}/distfiles/ascp2450.430 .; \
        ${CP} -pf ${PKGSRCDIR}/distfiles/ascp2550.430 .; \
        ${CP} -pf ${PKGSRCDIR}/distfiles/testpo.430 .;)

do-build:
	(cd ${WRKSRC}/build; \
	gmake;)

post-build:
	(cd ${WRKSRC}/data/JPL_ephemeris; \
	gmake asc2eph; \
	gmake ascii.430; \
	gmake de430.dat; \
	gmake ephtester; \
	gmake test; \
	gmake eph;)
	
pre-install:
	mkdir -p ${DESTDIR}${PREFIX}/bin; \
	mkdir -p ${DESTDIR}${PREFIX}/etc/oorb; \
	mkdir -p ${DESTDIR}${PREFIX}/lib; \
	mkdir -p ${DESTDIR}${PREFIX}/share/oorb; \
	mkdir -p ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \

do-install:
	${CP} ${WRKSRC}/bin/ephemeris_linking ${DESTDIR}${PREFIX}/bin; \
	${CP} ${WRKSRC}/bin/oorb ${DESTDIR}${PREFIX}/bin; \
	${CP} ${WRKSRC}/bin/orbit_linking ${DESTDIR}${PREFIX}/bin; \
	${CP} ${WRKSRC}/data/ET-UT.dat ${DESTDIR}${PREFIX}/share/oorb; \
	${CP} ${WRKSRC}/data/OBSCODE.dat ${DESTDIR}${PREFIX}/share/oorb; \
	${CP} ${WRKSRC}/data/TAI-UTC.dat ${DESTDIR}${PREFIX}/share/oorb; \
	${CP} ${WRKSRC}/data/de430.dat ${DESTDIR}${PREFIX}/share/oorb; \
	${CP} ${WRKSRC}/data/updateOBSCODE ${DESTDIR}${PREFIX}/bin; \
	${CP} ${WRKSRC}/doc/OpenOrb_Tutorial.pdf ${DESTDIR}${PREFIX}/share/oorb; \
	${CP} ${WRKSRC}/lib/liboorb.a ${DESTDIR}${PREFIX}/lib; \
	${CP} ${WRKSRC}/lib/liboorb.so ${DESTDIR}${PREFIX}/lib; \
	${CP} ${WRKSRC}/main/oorb.conf ${DESTDIR}${PREFIX}/etc/oorb; \
	${CP} ${WRKSRC}/gnuplot/cos_plot_car.gp ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \
	${CP} ${WRKSRC}/gnuplot/cos_plot_kep.gp ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \
	${CP} ${WRKSRC}/gnuplot/ls_plot.gp ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \
	${CP} ${WRKSRC}/gnuplot/sor_plot_car.gp ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \
	${CP} ${WRKSRC}/gnuplot/sor_plot_kep.gp ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \
	${CP} ${WRKSRC}/gnuplot/sor_plot_kep_nolog.gp ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \
	${CP} ${WRKSRC}/gnuplot/sor_plot_range.gp ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \
	${CP} ${WRKSRC}/gnuplot/vomcmc_plot_car.gp ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \
	${CP} ${WRKSRC}/gnuplot/vomcmc_plot_kep.gp ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \
	${CP} ${WRKSRC}/gnuplot/vov_plot_car.gp ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \
	${CP} ${WRKSRC}/gnuplot/vov_plot_kep.gp ${DESTDIR}${PREFIX}/share/oorb/gnuplot; \

# url2pkg-marker (please do not remove this line.)
.include "../../math/lapack/buildlink3.mk"
.include "../../lang/gcc12/buildlink3.mk"
.include "../../mk/bsd.pkg.mk"
