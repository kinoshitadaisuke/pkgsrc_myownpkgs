# $NetBSD$

GITHUB_TAG=	refs/tags/v${PKGVERSION_NOREV}
DISTNAME=	ephs-1.0.1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	python math
MASTER_SITES=	${MASTER_SITE_GITHUB:=josepenaz/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/josepenaz/ephs
COMMENT=	ALeRCE's Ephemeris
LICENSE=	mit

WRKSRC=	${WRKDIR}/${DISTNAME}

DEPENDS+=       ${PYPKGPREFIX}-pandas>=1.1.3:../../math/py-pandas
DEPENDS+=       ${PYPKGPREFIX}-astropy>=4.2:../../pkgsrc_myownpkgs/py-astropy
DEPENDS+=       ${PYPKGPREFIX}-jplephem>=0:../../pkgsrc_myownpkgs/py-jplephem
DEPENDS+=       ${PYPKGPREFIX}-rebound>=3.12.2:../../pkgsrc_myownpkgs/py-rebound

PYTHON_VERSIONS_INCOMPATIBLE=	27

BUILDLINK_API_DEPENDS.py-numpy+=	${PYPKGPREFIX}-numpy>=1.18.1

.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
