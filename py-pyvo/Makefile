# $NetBSD$

DISTNAME=	pyvo-1.7
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=p/pyvo/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pyvo.readthedocs.io/en/latest/
COMMENT=	Astropy affiliated Python module for accessing virtual observatories
LICENSE=	modified-bsd

PYTHON_VERSIONS_INCOMPATIBLE=	27

DEPENDS+=	${PYPKGPREFIX}-numpy-[0-9]*:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-requests>=2.25.0:../../devel/py-requests
DEPENDS+=	${PYPKGPREFIX}-astropy>=5.0:../../pkgsrc_myownpkgs/py-astropy
#DEPENDS+=	${PYPKGPREFIX}-astropy-helpers-[0-9]*:../../pkgsrc_myownpkgs/py-astropy-helpers
DEPENDS+=	${PYPKGPREFIX}-wheel-[0-9]*:../../devel/py-wheel

.include "../../lang/python/wheel.mk"
.include "../../math/py-numpy/buildlink3.mk"
.include "../../mk/bsd.pkg.mk"
