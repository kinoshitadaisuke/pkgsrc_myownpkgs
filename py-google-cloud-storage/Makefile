# $NetBSD$

DISTNAME=	google_cloud_storage-3.9.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/_cloud_/-cloud-/}
CATEGORIES=	net python
MASTER_SITES=	${MASTER_SITE_PYPI:=g/google_cloud_storage/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/google_cloud_storage/
COMMENT=	Google Cloud Storage API client library
LICENSE=	apache-2.0

DEPENDS+=	${PYPKGPREFIX}-google-auth>=2.26.1:../../security/py-google-auth
DEPENDS+=	${PYPKGPREFIX}-google-api-core>=2.27.0:../../devel/py-google-api-core
DEPENDS+=	${PYPKGPREFIX}-google-cloud-core>=2.4.2:../../pkgsrc_myownpkgs/py-google-cloud-core
DEPENDS+=	${PYPKGPREFIX}-google-resumable-media>=2.7.2:../../pkgsrc_myownpkgs/py-google-resumable-media
DEPENDS+=	${PYPKGPREFIX}-google-crc32c>=1.1.3:../../pkgsrc_myownpkgs/py-google-crc32c
DEPENDS+=	${PYPKGPREFIX}-requests>=2.22.0:../../devel/py-requests
DEPENDS+=	${PYPKGPREFIX}-grpcio>=1.75.1:../../net/py-grpcio
DEPENDS+=	${PYPKGPREFIX}-proto-plus>=1.25.0:../../devel/py-proto-plus
DEPENDS+=	${PYPKGPREFIX}-protobuf>=3.20.2:../../devel/py-protobuf

# url2pkg-marker (please do not remove this line.)
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
